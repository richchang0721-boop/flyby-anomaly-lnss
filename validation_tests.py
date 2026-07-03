"""
validation_tests.py — 自動化檢查

這裡的每一項檢查，都對應 2026-07-02 那一輪手動稽核裡真實抓到過的錯誤模式。
目的：讓同樣類型的錯誤下次由程式自動擋下來，不必再靠人工一個個案例肉眼查。

用法：
  python3 validation_tests.py results.json
"""

import sys
import json
import math


def check_altitude_vs_official(entry, tolerance_km=30):
    """對應教訓：δ_peri/perigee 抓錯時間點會讓高度差一個量級（JUICE 1天步長曾抓到472,600km）"""
    if entry.get("official_perigee_alt_km") is None or entry.get("perigee_altitude_km") is None:
        return None
    diff = abs(entry["perigee_altitude_km"] - entry["official_perigee_alt_km"])
    ok = diff <= tolerance_km
    return ("perigee_altitude", entry["name"], ok,
            f"diff={diff:.2f}km, tolerance={tolerance_km}km")


def check_declination_within_inclination_bound(entry, inclination_deg):
    """對應教訓：Galileo I 舊資料庫 δ_peri=-61.8° 超出軌道傾角142.9°允許的物理上限37.1°，
    這種矛盾本應該在數字產生的當下就被擋下來。"""
    bound = min(inclination_deg, 180 - inclination_deg)
    pos = abs(entry.get("delta_peri_position_deg", 0))
    ok = pos <= bound + 0.5  # 留一點數值誤差容忍
    return ("inclination_bound", entry["name"], ok,
            f"|δ_peri_pos|={pos:.2f}° vs 傾角上限{bound:.2f}°")


def check_confidence_flagged(entry):
    """對應教訓：Rosetta I 的 δᵢ 因低V∞收斂緩慢，精度較低但仍被使用。
    此檢查只確認每筆數值都有明確標註信心等級，不允許「沒說明就當作高信心」。"""
    has_i = "delta_i_confidence" in entry
    has_o = "delta_o_confidence" in entry
    ok = has_i and has_o
    return ("confidence_documented", entry["name"], ok,
            f"δᵢ標註={has_i}, δₒ標註={has_o}")


def check_disputed_values_flagged(entry):
    """對應教訓：Cassini觀測值有文獻分歧(-2.00 vs -0.5±0.5)，必須明確標註，不可只取其一當定值。"""
    if "dV_obs_disputed_alt_mm_s" not in entry:
        return None
    has_source = "dV_obs_disputed_source" in entry
    return ("disputed_value_documented", entry["name"], has_source,
            f"標註來源={has_source}")


def check_cosine_evenness_sanity(entry):
    """對應教訓：δₒ多次出現「量級相同、正負號相反」的情況，此本身不是錯誤
    （cos是偶函數，Anderson P1不受影響），但用來確認開發者理解這個特性，
    不會誤把符號翻轉當成需要修正的錯誤而重新調整。此檢查僅記錄，不判定通過/失敗。"""
    return None


def run_all_checks(results_path):
    with open(results_path, encoding="utf-8") as f:
        data = json.load(f)

    all_results = []
    for entry in data.get("flybys", []):
        for check_fn, kwargs in [
            (check_altitude_vs_official, {}),
            (check_confidence_flagged, {}),
            (check_disputed_values_flagged, {}),
        ]:
            r = check_fn(entry, **kwargs)
            if r:
                all_results.append(r)

        if "orbital_inclination_deg" in entry:
            r = check_declination_within_inclination_bound(
                entry, entry["orbital_inclination_deg"]
            )
            all_results.append(r)

    print(f"{'檢查項':22s}{'案例':15s}{'結果':8s}{'細節'}")
    print("-" * 80)
    n_fail = 0
    for check_name, case_name, passed, detail in all_results:
        status = "✓ PASS" if passed else "✗ FAIL"
        if not passed:
            n_fail += 1
        print(f"{check_name:22s}{case_name:15s}{status:8s}{detail}")

    print("-" * 80)
    print(f"總計 {len(all_results)} 項檢查，{n_fail} 項失敗")
    return n_fail == 0


if __name__ == "__main__":
    path = sys.argv[1] if len(sys.argv) > 1 else "results.json"
    ok = run_all_checks(path)
    sys.exit(0 if ok else 1)
