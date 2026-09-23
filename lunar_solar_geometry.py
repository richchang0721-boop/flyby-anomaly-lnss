"""
lunar_solar_geometry.py — 計算 JUICE 近地點時刻的日—地—月幾何
（對應 05a_JUICE_2026_Boundary_Conditions.md 第 4 節與 5.4 節）

規則（與 reconstruct.py 相同）：
  05a 第 4 節的所有數值只允許由這個程式計算。
  任何人（包含任何版本的 LLM）不可以「憑文字重新算一次」這些數字並回報新結果。
  若懷疑有誤：重新查詢 Horizons → 用這份程式碼重跑 → 更新 results.json + CHANGELOG.md。

用法：
  python3 lunar_solar_geometry.py <JUICE.txt> <Moon.txt> <Sun.txt>
  python3 lunar_solar_geometry.py <JUICE.txt> <Moon.txt> <Sun.txt> --write results.json

輸入（三份 Horizons VECTORS 輸出，設定必須完全一致）：
  - Center：500@399（Geocentric, BODY CENTER）
  - Reference frame：ICRF，reference plane = x-y axes of reference frame (equatorial)
  - 步長：1 分鐘
  - CSV 格式
  - Moon / Sun 的時間範圍必須涵蓋最近一次滿月（建議 2026-09-24 00:00 至 2026-10-01 00:00 TDB）
  - JUICE 檔可直接沿用現有 data/raw/ 中的檔案（只要時間範圍包含近地點）

時間系統說明：
  - Horizons VECTORS 的時間欄為 TDB。
  - UTC 換算採 TT − UTC = 69.184 s（TAI − UTC = 37 s）。
    若 IERS Bulletin C 在 2026-09 之前宣告新閏秒，須修改 TT_MINUS_UTC_S。
  - TDB − TT 的週期項 < 2 ms，忽略。
  - UT1 以 UTC 近似（|UT1 − UTC| < 0.9 s → GMST 誤差 < 0.004°）。

滿月定義：
  地心黃經差 λ_Moon − λ_Sun = 180°。
  使用 Horizons 預設的幾何向量（無光行時／光行差修正），
  所以結果與天文年曆（視黃經）可能相差數分鐘。這是定義差異，不是錯誤；
  輸出中會註明所用定義。
"""

import sys
import json
import math
import argparse
from datetime import datetime, timedelta, timezone

sys.path.insert(0, ".")
from constants import R_EARTH_KM
from reconstruct import parse_horizons_vectors, find_precise_perigee, speed

# ── 本檔專用常數 ────────────────────────────────────────────────
# 僅用於「潮汐加速度環境記錄」，不進入任何預測。
# 建議核對 JPL DE440 文件後，移入 constants.py 作為唯一來源。
GM_MOON_KM3_S2 = 4902.800118          # DE440（待核對）
GM_SUN_KM3_S2 = 1.32712440041e11      # DE440（待核對）
OBLIQUITY_J2000_DEG = 84381.406 / 3600.0  # IAU 2006 ε₀
TT_MINUS_UTC_S = 69.184               # 32.184 + 37（待對照 IERS Bulletin C）

RESULT_KEY = "JUICE_2026_boundary_conditions"


# ── 向量工具 ────────────────────────────────────────────────────
def vec(row, kind="r"):
    if kind == "r":
        return (row["x"], row["y"], row["z"])
    return (row["vx"], row["vy"], row["vz"])


def dot(a, b):
    return sum(i * j for i, j in zip(a, b))


def norm(a):
    return math.sqrt(dot(a, a))


def sub(a, b):
    return tuple(i - j for i, j in zip(a, b))


def scale(a, s):
    return tuple(i * s for i in a)


def angle_deg(a, b):
    c = dot(a, b) / (norm(a) * norm(b))
    return math.degrees(math.acos(max(-1.0, min(1.0, c))))


def ra_dec_deg(a):
    r = norm(a)
    return (math.degrees(math.atan2(a[1], a[0])) % 360.0,
            math.degrees(math.asin(a[2] / r)))


def ecliptic_longitude_deg(a):
    """赤道 ICRF → J2000 黃道，回傳黃經（度）。
    λ_Moon − λ_Sun 對黃道定義的歲差不敏感（兩者同步旋轉），故用 J2000 黃道即可。"""
    e = math.radians(OBLIQUITY_J2000_DEG)
    x = a[0]
    y = a[1] * math.cos(e) + a[2] * math.sin(e)
    return math.degrees(math.atan2(y, x)) % 360.0


def wrap180(d):
    return (d + 180.0) % 360.0 - 180.0


# ── 時間工具 ────────────────────────────────────────────────────
def parse_horizons_date(s):
    s = s.replace("A.D.", "").strip()
    for fmt in ("%Y-%b-%d %H:%M:%S.%f", "%Y-%b-%d %H:%M:%S", "%Y-%b-%d %H:%M"):
        try:
            return datetime.strptime(s, fmt)
        except ValueError:
            continue
    raise ValueError(f"無法解析 Horizons 日期字串：{s}")


def jd_from_datetime(dt):
    """naive datetime（視為該時間系統下的時刻）→ Julian Date"""
    epoch = datetime(1970, 1, 1)
    return 2440587.5 + (dt - epoch).total_seconds() / 86400.0


def earth_rotation_angle_deg(jd_ut1):
    du = jd_ut1 - 2451545.0
    return (360.0 * (0.7790572732640 + 1.00273781191135448 * du)) % 360.0


def gmst_deg(jd_ut1, jd_tt):
    """IAU 2006 GMST（取至 T² 項，精度遠優於本用途所需）"""
    t = (jd_tt - 2451545.0) / 36525.0
    poly_arcsec = 0.014506 + 4612.156534 * t + 1.3915817 * t * t
    return (earth_rotation_angle_deg(jd_ut1) + poly_arcsec / 3600.0) % 360.0


# ── 物理量 ──────────────────────────────────────────────────────
def tidal_acceleration(r_sc, r_body, gm):
    """第三體對地心座標中太空船的潮汐（差分）加速度，km/s²"""
    d = sub(r_body, r_sc)
    return sub(scale(d, gm / norm(d) ** 3), scale(r_body, gm / norm(r_body) ** 3))


def check_header(header, label):
    center = (header.get("center") or "").upper()
    if "EARTH" not in center and "399" not in center:
        raise ValueError(f"{label}：Center 不是地心（實際：{header.get('center')}），禁止繼續計算。")
    frame = (header.get("ref_frame") or "").upper()
    if "ICRF" not in frame:
        raise ValueError(f"{label}：Reference frame 不是 ICRF（實際：{header.get('ref_frame')}）。")


def index_by_date(rows):
    return {r["date"]: r for r in rows}


def find_full_moons(moon_rows, sun_by_date):
    """在共同時間點上找 λ_Moon − λ_Sun 穿越 180° 的時刻（線性內插）"""
    series = []
    for m in moon_rows:
        s = sun_by_date.get(m["date"])
        if s is None:
            continue
        dt = parse_horizons_date(m["date"])
        dl = wrap180(ecliptic_longitude_deg(vec(m)) - ecliptic_longitude_deg(vec(s)) - 180.0)
        series.append((dt, dl))

    crossings = []
    for (t0, d0), (t1, d1) in zip(series, series[1:]):
        # 月球黃經相對太陽持續增加 → dl 由負轉正；排除 ±180 的包繞跳變
        if d0 < 0.0 <= d1 and (d1 - d0) < 10.0:
            frac = -d0 / (d1 - d0)
            crossings.append(t0 + (t1 - t0) * frac)
    return crossings, (series[0][0], series[-1][0]) if series else (None, None)


# ── 主流程 ──────────────────────────────────────────────────────
def compute(juice_path, moon_path, sun_path):
    hj, juice = parse_horizons_vectors(juice_path)
    hm, moon = parse_horizons_vectors(moon_path)
    hs, sun = parse_horizons_vectors(sun_path)
    for h, label in ((hj, "JUICE"), (hm, "Moon"), (hs, "Sun")):
        check_header(h, label)

    idx, peri = find_precise_perigee(juice)
    moon_by_date = index_by_date(moon)
    sun_by_date = index_by_date(sun)
    if peri["date"] not in moon_by_date or peri["date"] not in sun_by_date:
        raise ValueError(
            f"Moon/Sun 檔中找不到與 JUICE 近地點完全相同的時間點（{peri['date']}）。"
            " 三份查詢必須使用相同的步長與起點對齊。"
        )
    m = moon_by_date[peri["date"]]
    s = sun_by_date[peri["date"]]

    r_sc, v_sc = vec(peri, "r"), vec(peri, "v")
    r_m, r_s = vec(m), vec(s)

    # 日—地—月
    elongation = angle_deg(r_m, r_s)                        # 在地心看，日月夾角
    phase_angle = angle_deg(sub(r_s, r_m), scale(r_m, -1))  # 在月球看，日地夾角
    illuminated = (1.0 + math.cos(math.radians(phase_angle))) / 2.0

    # 時間
    t_peri_tdb = parse_horizons_date(peri["date"])
    t_peri_utc = t_peri_tdb - timedelta(seconds=TT_MINUS_UTC_S)
    jd_tt = jd_from_datetime(t_peri_tdb)
    jd_ut1 = jd_from_datetime(t_peri_utc)

    full_moons, (win_start, win_end) = find_full_moons(moon, sun_by_date)
    nearest_fm = min(full_moons, key=lambda t: abs((t - t_peri_tdb).total_seconds())) if full_moons else None

    moon_ra, moon_dec = ra_dec_deg(r_m)
    sun_ra, sun_dec = ra_dec_deg(r_s)

    a_moon = tidal_acceleration(r_sc, r_m, GM_MOON_KM3_S2)
    a_sun = tidal_acceleration(r_sc, r_s, GM_SUN_KM3_S2)
    r_hat = scale(r_sc, 1.0 / norm(r_sc))
    v_hat = scale(v_sc, 1.0 / norm(v_sc))
    a_tot = tuple(i + j for i, j in zip(a_moon, a_sun))

    km_to_m = 1000.0
    result = dict(
        purpose="05a Section 4 / 5.4 environmental boundary conditions — record only, not a prediction",
        source_files=dict(juice=juice_path, moon=moon_path, sun=sun_path),
        horizons_ref_frame=dict(juice=hj.get("ref_frame"), moon=hm.get("ref_frame"), sun=hs.get("ref_frame")),
        horizons_center=dict(juice=hj.get("center"), moon=hm.get("center"), sun=hs.get("center")),
        query_step=dict(juice=hj.get("step"), moon=hm.get("step"), sun=hs.get("step")),

        perigee_time_tdb=peri["date"],
        perigee_time_utc_approx=t_peri_utc.strftime("%Y-%m-%d %H:%M:%S") + " (TT−UTC = %.3f s)" % TT_MINUS_UTC_S,
        perigee_altitude_km_crosscheck=round(peri["r"] - R_EARTH_KM, 2),
        perigee_speed_kms_crosscheck=round(speed(peri), 4),

        full_moon_definition="geometric geocentric ecliptic longitude difference = 180° (no light-time/aberration)",
        full_moon_search_window_tdb=[str(win_start), str(win_end)],
        full_moon_times_found_tdb=[t.strftime("%Y-%m-%d %H:%M:%S") for t in full_moons],
        nearest_full_moon_tdb=nearest_fm.strftime("%Y-%m-%d %H:%M:%S") if nearest_fm else None,
        hours_from_full_moon_to_perigee=(
            round((t_peri_tdb - nearest_fm).total_seconds() / 3600.0, 2) if nearest_fm else None
        ),

        sun_earth_moon_elongation_deg=round(elongation, 3),
        lunar_phase_angle_deg=round(phase_angle, 3),
        lunar_illuminated_fraction=round(illuminated, 4),
        earth_moon_distance_km=round(norm(r_m), 1),
        earth_sun_distance_km=round(norm(r_s), 0),

        moon_ra_deg=round(moon_ra, 4),
        moon_dec_deg=round(moon_dec, 4),
        sun_ra_deg=round(sun_ra, 4),
        sun_dec_deg=round(sun_dec, 4),

        angle_moon_vs_perigee_position_deg=round(angle_deg(r_m, r_sc), 3),
        angle_moon_vs_perigee_velocity_deg=round(angle_deg(r_m, v_sc), 3),
        angle_sun_vs_perigee_position_deg=round(angle_deg(r_s, r_sc), 3),
        angle_sun_vs_perigee_velocity_deg=round(angle_deg(r_s, v_sc), 3),

        tidal_accel_at_perigee_note="Newtonian third-body differential acceleration; assumed absorbed by conventional OD (05a §5.1). Record only.",
        tidal_accel_moon_m_s2=round(norm(a_moon) * km_to_m, 12),
        tidal_accel_sun_m_s2=round(norm(a_sun) * km_to_m, 12),
        tidal_accel_total_m_s2=round(norm(a_tot) * km_to_m, 12),
        tidal_accel_total_radial_m_s2=round(dot(a_tot, r_hat) * km_to_m, 12),
        tidal_accel_total_along_velocity_m_s2=round(dot(a_tot, v_hat) * km_to_m, 12),
        gm_constants_used=dict(moon=GM_MOON_KM3_S2, sun=GM_SUN_KM3_S2, status="to be verified against DE440 and moved to constants.py"),

        earth_rotation_angle_deg=round(earth_rotation_angle_deg(jd_ut1), 4),
        gmst_deg=round(gmst_deg(jd_ut1, jd_tt), 4),
        gmst_note="IAU 2006, UT1 ≈ UTC",

        computed_at=datetime.now(timezone.utc).isoformat(),
    )

    warnings = []
    if nearest_fm is None:
        warnings.append("查詢範圍內未找到滿月。請擴大 Moon/Sun 查詢範圍（建議 2026-09-24 至 2026-10-01）。")
    if abs(elongation + phase_angle - 180.0) > 1.0:
        warnings.append("elongation + phase angle 偏離 180° 超過 1°，請檢查輸入（地月距離遠小於日地距離時兩者應近似互補）。")
    result["warnings"] = warnings
    return result


def main():
    p = argparse.ArgumentParser(description="JUICE 2026 近地點日—地—月幾何（05a 第 4 節）")
    p.add_argument("juice")
    p.add_argument("moon")
    p.add_argument("sun")
    p.add_argument("--write", metavar="RESULTS_JSON",
                   help=f"將結果寫入 results.json 的 '{RESULT_KEY}' 鍵（會覆寫該鍵，其他鍵不動）")
    args = p.parse_args()

    result = compute(args.juice, args.moon, args.sun)
    print(json.dumps(result, indent=2, ensure_ascii=False))

    if args.write:
        with open(args.write, encoding="utf-8") as f:
            data = json.load(f)
        if not isinstance(data, dict):
            raise ValueError("results.json 頂層不是 dict，未寫入。請手動合併。")
        data[RESULT_KEY] = result
        with open(args.write, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        print(f"\n已寫入 {args.write} → '{RESULT_KEY}'。請同步在 CHANGELOG.md 記錄。")

    if result["warnings"]:
        print("\n⚠️  " + "\n⚠️  ".join(result["warnings"]))


if __name__ == "__main__":
    main()
