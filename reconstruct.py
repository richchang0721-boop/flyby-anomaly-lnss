"""
reconstruct.py — 從 JPL Horizons 原始輸出重建飛掠幾何參數

規則（重要）：
  這個檔案是「δᵢ、δₒ、δ_peri、近地點高度」這些數字唯一被允許計算出來的地方。
  任何人（包含任何版本的 LLM）review 這份研究時：
    - 可以檢查這份程式碼的邏輯是否正確
    - 不可以「憑文字重新算一次」δᵢ/δₒ/δ_peri 這些數字並回報新結果
    - 若懷疑某個結果有誤，正確做法是：重新查詢 Horizons → 用這份程式碼重跑 → 更新 results.json + CHANGELOG.md
  這條規則存在的原因：2026-07-02 發現舊資料庫的 δ_peri 對全部 7 個歷史飛掠都是錯的，
  且沒有任何計算方法記錄，起因就是數字曾經以「文字推理/印象」的方式產生並被當成真值使用。

用法：
  python3 reconstruct.py <horizons_output.txt>

輸入格式：
  JPL Horizons API/網頁輸出，VECTORS 星曆，Reference plane 必須是
  "x-y axes of reference frame (equatorial...)" ── 絕對不可以是 ecliptic。
  Center 必須是 Geocentric (500@399)，不可是任何地面觀測站。

輸出：
  一個 dict，包含精確近地點時刻、高度、位置赤緯、速度赤緯、
  以及頭尾漸近段的逐日速度赤緯數列（供人工目視確認是否已收斂）。
"""

import re
import sys
import json
import math
from datetime import datetime, timezone

sys.path.insert(0, ".")
from constants import R_EARTH_KM, ANDERSON_K, P2_NODE_DEG


def parse_horizons_vectors(filepath):
    """解析 Horizons VECTORS 輸出，回傳 (header_info, rows)。
    rows 為 list of dict: {date, x, y, z, vx, vy, vz, r}（單位 km, km/s）"""
    with open(filepath, encoding="utf-8", errors="replace") as f:
        text = f.read()

    header = {}
    for key, pattern in [
        ("target", r"Target body name:\s*(.+)"),
        ("center", r"Center body name:\s*(.+)"),
        ("center_site", r"Center-site name:\s*(.+)"),
        ("start", r"Start time\s*:\s*(.+)"),
        ("stop", r"Stop  time\s*:\s*(.+)"),
        ("step", r"Step-size\s*:\s*(.+)"),
        ("ref_frame", r"Reference frame\s*:\s*(.+)"),
    ]:
        m = re.search(pattern, text)
        header[key] = m.group(1).strip() if m else None

    # 座標系與中心點的安全檢查（不通過就直接報錯，不允許往下算）
    if header["center_site"] and "BODY CENTER" not in header["center_site"].upper():
        raise ValueError(
            f"Center-site 不是 BODY CENTER（實際: {header['center_site']}）。"
            " 用地面觀測站當中心會引入公里級視差誤差，禁止繼續計算。"
        )
    if header["ref_frame"] and "ICRF" not in header["ref_frame"].upper():
        print(f"⚠️  警告：Reference frame = {header['ref_frame']}，非 ICRF，請確認是否為赤道座標。")

    start = text.index("$$SOE")
    end = text.index("$$EOE")
    block = text[start + 5 : end]

    rows = []
    for line in block.strip().split("\n"):
        parts = [p.strip() for p in line.split(",") if p.strip() != ""]
        if len(parts) < 8:
            continue
        date = parts[1]
        x, y, z, vx, vy, vz = map(float, parts[2:8])
        r = math.sqrt(x**2 + y**2 + z**2)
        rows.append(dict(date=date, x=x, y=y, z=z, vx=vx, vy=vy, vz=vz, r=r))

    if not rows:
        raise ValueError("未在檔案中找到 $$SOE/$$EOE 之間的資料列，檢查輸入格式。")

    return header, rows


def declination_position(row):
    """位置赤緯 (度)：arcsin(z/r)"""
    return math.degrees(math.asin(row["z"] / row["r"]))


def ra_position(row):
    """位置赤經 (度, 0-360)：atan2(y,x)"""
    ra = math.degrees(math.atan2(row["y"], row["x"]))
    return ra % 360


def ra_velocity(row):
    """速度方向赤經 (度, 0-360)：atan2(vy,vx)"""
    ra = math.degrees(math.atan2(row["vy"], row["vx"]))
    return ra % 360


def declination_velocity(row):
    """速度赤緯 (度)：arcsin(vz/|v|)"""
    vmag = math.sqrt(row["vx"] ** 2 + row["vy"] ** 2 + row["vz"] ** 2)
    return math.degrees(math.asin(row["vz"] / vmag))


def speed(row):
    return math.sqrt(row["vx"] ** 2 + row["vy"] ** 2 + row["vz"] ** 2)


def find_precise_perigee(rows):
    """找地心距離最小的那一列（前提：輸入步長夠細，建議1分鐘）"""
    best = min(rows, key=lambda r: r["r"])
    idx = rows.index(best)
    return idx, best


def find_asymptote_window(rows, idx_perigee, direction, window_days=1, step_per_day=1440):
    """粗略抓漸近段：direction='in' 抓 perigee 之前最遠的穩定段，'out' 抓之後。
    這是輔助函數，實際判斷是否已收斂仍需人工目視 daily_declination_trend 的輸出。
    """
    n = len(rows)
    if direction == "in":
        i = max(0, idx_perigee - window_days * step_per_day)
    else:
        i = min(n - 1, idx_perigee + window_days * step_per_day)
    return rows[i]


def find_asymptote_auto(rows, idx_perigee, direction, step_per_day=1440, min_days_from_perigee=3):
    """自動偵測漸近段收斂點:在遠離近地點(min_days_from_perigee天以上)的區域,
    找逐日赤緯變化量(|dδ/dt|)最小的那一天,回傳該日的完整row。
    這取代了先前用肉眼判斷"哪天看起來穩定"的做法,結果可重現、不依賴人工判斷。
    """
    n = len(rows)
    min_offset = min_days_from_perigee * step_per_day

    if direction == "in":
        candidates = list(range(0, max(0, idx_perigee - min_offset), step_per_day))
    else:
        candidates = list(range(idx_perigee + min_offset, n, step_per_day))

    if len(candidates) < 2:
        # 資料不夠遠離近地點,退回邊界點並標記低信心
        idx = candidates[0] if candidates else (0 if direction == "in" else n - 1)
        return rows[idx], "low_confidence_insufficient_range"

    best_idx = None
    best_slope = None
    for i in range(len(candidates) - 1):
        idx_a, idx_b = candidates[i], candidates[i + 1]
        d_a = declination_velocity(rows[idx_a])
        d_b = declination_velocity(rows[idx_b])
        slope = abs(d_b - d_a)
        if best_slope is None or slope < best_slope:
            best_slope = slope
            best_idx = idx_a

    confidence = "high" if best_slope < 0.05 else ("medium" if best_slope < 0.3 else "low")
    return rows[best_idx], confidence


def extract_asymptotes(rows, idx_perigee, **kwargs):
    """自動抽取入射/出射漸近段的完整資訊(δ, RA, V∞),回傳dict"""
    row_in, conf_in = find_asymptote_auto(rows, idx_perigee, "in", **kwargs)
    row_out, conf_out = find_asymptote_auto(rows, idx_perigee, "out", **kwargs)
    return dict(
        delta_i_deg=round(declination_velocity(row_in), 4),
        ra_i_deg=round(ra_velocity(row_in), 4),
        v_inf_i_kms=round(speed(row_in), 4),
        delta_i_date=row_in["date"],
        delta_i_confidence=conf_in,
        delta_o_deg=round(declination_velocity(row_out), 4),
        ra_o_deg=round(ra_velocity(row_out), 4),
        v_inf_o_kms=round(speed(row_out), 4),
        delta_o_date=row_out["date"],
        delta_o_confidence=conf_out,
    )


def daily_declination_trend(rows, step_per_day=1440):
    """逐日速度赤緯與距離，供人工確認漸近段是否收斂"""
    out = []
    for i in range(0, len(rows), step_per_day):
        row = rows[i]
        out.append(
            dict(
                date=row["date"],
                r_km=round(row["r"], 1),
                speed_kms=round(speed(row), 4),
                vel_declination_deg=round(declination_velocity(row), 3),
            )
        )
    return out


def anderson_p1_mm_s(v_inf_kms, delta_i_deg, delta_o_deg):
    """標準 Anderson P1 預測值 (mm/s)。K 從 constants.py 匯入，非重新定義。"""
    diff = math.cos(math.radians(delta_i_deg)) - math.cos(math.radians(delta_o_deg))
    return v_inf_kms * 1e6 * ANDERSON_K * diff


def validate_perigee_altitude(alt_km, official_alt_km, tolerance_km=30):
    """自動檢查：重建高度與官方值誤差是否在合理範圍內"""
    diff = abs(alt_km - official_alt_km)
    ok = diff <= tolerance_km
    return dict(diff_km=round(diff, 2), tolerance_km=tolerance_km, passed=ok)


def reconstruct_flyby(filepath, official_alt_km=None, name=None):
    """主流程：輸入一份 Horizons 檔案，輸出完整重建結果 dict"""
    header, rows = parse_horizons_vectors(filepath)
    idx, peri = find_precise_perigee(rows)

    result = dict(
        name=name or header.get("target"),
        source_file=filepath,
        horizons_target=header.get("target"),
        horizons_center=header.get("center"),
        horizons_ref_frame=header.get("ref_frame"),
        query_step=header.get("step"),
        perigee_time_tdb=peri["date"],
        perigee_r_km=round(peri["r"], 2),
        perigee_altitude_km=round(peri["r"] - R_EARTH_KM, 2),
        perigee_speed_kms=round(speed(peri), 4),
        delta_peri_position_deg=round(declination_position(peri), 4),
        ra_peri_position_deg=round(ra_position(peri), 4),
        delta_peri_velocity_deg=round(declination_velocity(peri), 4),
        ra_peri_velocity_deg=round(ra_velocity(peri), 4),
        daily_trend=daily_declination_trend(rows),
        reconstructed_at=datetime.now(timezone.utc).isoformat(),
    )
    result.update(extract_asymptotes(rows, idx))

    if official_alt_km is not None:
        result["altitude_validation"] = validate_perigee_altitude(
            result["perigee_altitude_km"], official_alt_km
        )

    return result


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("用法: python3 reconstruct.py <horizons_output.txt> [官方近地點高度km]")
        sys.exit(1)

    filepath = sys.argv[1]
    official_alt = float(sys.argv[2]) if len(sys.argv) > 2 else None

    result = reconstruct_flyby(filepath, official_alt_km=official_alt)

    # 只印摘要，完整逐日趨勢資料留給人工在 daily_trend 裡自行檢查收斂性
    summary = {k: v for k, v in result.items() if k != "daily_trend"}
    print(json.dumps(summary, indent=2, ensure_ascii=False))
    print(f"\n（完整逐日收斂趨勢共 {len(result['daily_trend'])} 筆，請人工確認 δᵢ/δₒ 是否已平穩，"
          f"這一步無法自動化——收斂快慢因 V∞ 而異，見 Rosetta I 案例的教訓）")
