"""
constants.py — 物理常數的唯一權威來源 (Single Source of Truth)

規則：
1. 任何計算腳本都必須從這裡 import 常數，不可在其他檔案裡重複定義或硬編碼。
2. 修改任何數值都必須在 CHANGELOG.md 留下記錄（日期、舊值、新值、原因、來源）。
3. LLM review 這份檔案時，只能檢查數值是否與標註來源一致，不可「憑印象」修改。
"""

# ---- 基本物理常數 ----
G = 6.674e-11           # 萬有引力常數 (m^3 kg^-1 s^-2)
C = 2.998e8              # 光速 (m/s)
HBAR = 1.0546e-34        # 約化蒲朗克常數 (J*s)
EV = 1.602e-19           # 1 電子伏特 (J)

# ---- 地球常數 ----
R_EARTH_KM = 6371.0                # 地球平均半徑 (km)
R_EARTH_M = R_EARTH_KM * 1000
M_EARTH = 5.972e24                 # 地球質量 (kg)
OMEGA_EARTH = 7.292115e-5          # 地球自轉角速度 (rad/s)
I_EARTH = 8.034e37                 # 地球轉動慣量 (kg*m^2), 0.3307*M*R^2
J_EARTH = I_EARTH * OMEGA_EARTH    # 地球角動量 (kg*m^2/s)

# ---- Anderson 飛掠異常公式常數 ----
ANDERSON_K = 2 * OMEGA_EARTH * R_EARTH_M / C   # = 2*omega*R/c，約 3.097e-6

# ---- LNSS 框架推導值（非基本常數，是本框架的擬合/推導結果，來源見 04_Mathematics.md）----
B_MAIN_KM = 16076.0                # 背景場主要衰減長度 (km)，體積積分擬合 Anderson 係數得出
KAPPA_MAIN = 1 / (B_MAIN_KM * 1000)  # 對應波數 (1/m)

# ---- P2 節點（精確值，非擬合）----
import math
P2_NODE_DEG = math.degrees(math.acos(1 / math.sqrt(3)))  # = 54.7356...度

# ---- 版本記錄 ----
__version__ = "1.0.0"
__last_updated__ = "2026-07-02"
__changelog_ref__ = "見 CHANGELOG.md"
