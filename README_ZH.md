# LNSS Framework for Earth Flyby Anomaly

**Author:** Rich Chang (2026)  
**Cite as:** Chang, R. (2026). *LNSS Framework for Earth Flyby Anomaly*. GitHub: github.com/[your-account]/flyby-anomaly-lnss  
**License:** CC0 v1.0 Universal  
**Version:** v1.4 | **Created:** 2026-06-27 | **Collaborators:** Claude (Anthropic), GPT (OpenAI)

> ⚠️ **Sealed predictions recorded 2026-06-28.**  
> JUICE Earth flyby verification: **2026-09-28/29** | Europa Clipper: **2026-12-03**

---

## Research Question

> **Why do some hyperbolic Earth flybys exhibit unexplained mm/s-scale velocity anomalies while closed orbits do not?**

## Goal

> **Explain the Earth flyby anomaly using the smallest possible extension to known gravitational physics.**

---

## 30-Second Summary

```
Observation  →  Constraints  →  Mathematics  →  Hypothesis
```

The Earth flyby anomaly (Anderson et al. 2008) refers to unexplained mm/s-scale
velocity discrepancies in hyperbolic spacecraft trajectories past Earth.
This repository develops the **LNSS (Local Nonlinear Spatial Structure) /
Perturbation Model** framework to explain these anomalies using a gravitational
vector field grounded in General Relativity.

**Key results:**
- Closed orbits (LEO/GPS/ISS): ΔV ≡ 0 by topology (proven)
- Anomaly driver: |P₂(cosδ_peri)| — orbital symmetry, not field strength
- Threshold: |P₂| < 0.06 → unobservable; |P₂| > 0.06 → |ΔV| ≈ 19.3×|P₂| mm/s
- Factor of 2 in Anderson formula: two-way Doppler tracking (signal traverses Earth→SC→Earth)
- Unique unknown: background field wavenumber κ = 1/B_main = 1/16,076 km

---

## 研究結構（30 秒版本）

```
Observation
    ↓
Constraints
    ↓
Mathematics
    ↓
Hypothesis
```

詳細內容見各章節。

## 研究結構（完整版）

```
Core Observation
  └─ Anderson Formula：ΔV = V∞·(2ωR/c)·(cosδᵢ − cosδₒ)（已觀測，★★★★★）
       │
       ▼
Boundary Interpretation
  └─ Anderson 公式是路徑積分的精確邊界項（數學推導，★★★★☆）
       │
       ▼
Candidate PDE
  └─ Helmholtz ∇²Ψ + k²Ψ = S（唯一通過五公設，★★★☆☆）
       │
       ▼
Statistical Signals
  ├─ P₂(cosδ_peri) vs |dV|：r = 0.852（Correlative，★★☆☆☆）
  └─ ap vs dV：r = −0.72（Correlative，★★☆☆☆）
       │
       ▼
Possible Physical Interpretation（Perturbation Model）
  └─ 宇宙存在大尺度背景場 Ψ_bg
     地球不是「創造」LNSS，而是「擾動」背景場
     地球自轉形成 P₁/P₂ 局部模式
     太陽風（ap）調制有效振幅
     → Flyby anomaly 是擾動場的路徑積分（概念假說，★☆☆☆☆）
```

## 框架的根本轉變：Source Model → Perturbation Model

**舊框架（Source Model）：**
```
地球自轉 → 創造 LNSS 場
Helmholtz 的源項 S = 地球角動量
遠場邊界條件：Ψ → 0
```

**新框架（Perturbation Model）：**
```
宇宙背景場 Ψ_bg（均勻，方向由 CMB 決定）
        │
        ▼ 地球質量+自轉 → 局部擾動
        │
        ▼ 形成 P₁/P₂ 局部模式（Helmholtz 描述擾動場）
        │
        ▼ 太陽風（ap）調制振幅
        │
        ▼ Flyby anomaly
```

**這個轉變解決了三個懸案：**
- k² 的物理來源 = 背景場的「曲率」，不需要電漿或新粒子
- Busack 的 CMB 方向 = 背景場的優先方向，自然進入邊界條件
- **Anderson 公式無高度項 = 主場衰減長度遠大於飛掠高度，場在 300-2000 km 幾乎不變**（2026-06-27 新確立）

**兩個衰減尺度的分離（關鍵洞察）：**
```
Anderson 主場（δΨ_P₁）：衰減長度 B_main >> 飛掠高度（幾千 km）
                         → Anderson 公式無高度修正項 ✓

Busack 次要場（δΨ_CMB）：衰減長度 B_Busack = 394 km
                         → Busack 公式的 B 參數 ✓
```

---

## 檔案結構

```
FlybyResearch/
├── README.md              ← 本文件（索引 + 核心主張）
├── 01_Observations.md     ← 飛掠數據、行星距離、太陽活動
├── 02_Constraints.md      ← 觀測約束、五公設、已排除假說
├── 03_Hypotheses.md       ← 假說架構、三層場、RQ7、臨界形成
├── 04_Mathematics.md      ← Anderson、Boundary Term、Helmholtz、Busack
├── 05_Predictions.md      ← 密封預測（JUICE、Europa Clipper、P₃）
├── 06_Falsification.md    ← 可偽證條件
├── 07_Open_Problems.md    ← RQ1-RQ8、最高優先的下一步
└── Appendix_Data.md       ← 符號表、常數、文獻、版本歷史
```

---

## 證據等級摘要

| 結論 | ★ | 類別 |
|------|---|------|
| Anderson 公式 | ★★★★★ | Observation |
| Boundary Term 解釋 | ★★★★☆ | Mathematical |
| Helmholtz 球諧自然湧現 | ★★★★☆ | Mathematical |
| **封閉軌道 ΔV ≡ 0（拓樸定理）** | **★★★★★** | **Mathematical（2026-06-28）** |
| **因子 2 = 雙程 Doppler 追蹤（候選解答）** | **★★★☆☆** | **Mathematical（2026-06-28）** |
| **體積積分 η=1（不需要放大機制）** | **★★★★☆** | **Mathematical（2026-06-27）** |
| **GPS 無信號 = 框架預測一致** | **★★★☆☆** | **Observational+Mathematical** |
| **B_main = 16,076 km（背景場波數 k 的倒數）** | **★★☆☆☆** | **Mathematical+Correlative** |
| **兩個衰減尺度分離（Anderson 主場 vs Busack 次要場）** | **★★★☆☆** | **Mathematical** |
| **Ψ 是向量場（GEM A_φ）** | **★★★★☆** | **Mathematical** |
| **GR sinθ 結構與 Anderson 一致** | **★★★★☆** | **Mathematical** |
| **GR sinθ 結構與 Anderson 一致** | **★★★★☆** | **Mathematical** |
| Helmholtz 候選 PDE | ★★★☆☆ | Statistical |
| **|P₂|_c ≈ 0.06 臨界值（7/7 分類準確）** | **★★☆☆☆** | **Correlative（2026-06-28）** |
| P₂ 無風帶（±54.7°，r=0.852）| ★★☆☆☆ | Correlative |
| ap 指數與 dV（r=−0.72，次要修正因子）| ★★☆☆☆ | Correlative |
| 太陽風截斷 plasmasphere 機制 | ✗ 已排除 | Mathematical |
| ap 的物理機制（RQ13）| 次要效應，機制開放 | Open Problem |
| 兩分量假說（Anderson + Busack）| ★★☆☆☆ | Correlative |
| 電離層 F 層作為 k² 來源 | ★★☆☆☆ | Correlative |
| 暗物質+等離子體複合介質假說（局部暗物質差 100 倍）| ★☆☆☆☆ | Conceptual |
| LNSS / 空間介質 | ★☆☆☆☆ | Conceptual |
| **Perturbation Model（背景場+局部擾動）** | **★☆☆☆☆** | **Conceptual（2026-06-27 新增）** |
| LNSS 自發形成（卡門渦街類比）| ★☆☆☆☆ | Conceptual |

**等級定義：**
★★★★★ Observation｜★★★★☆ Mathematical｜★★★☆☆ Statistical｜★★☆☆☆ Correlative｜★☆☆☆☆ Conceptual

---

## 最高優先的下一步

1. **嚴格推導雙程 Doppler 的因子 2**（RQ2）——確認往返路徑積分嚴格相等
2. **推導 κ = 1/B_main 的理論來源**（RQ12）——背景場 Ψ_bg 的唯一未知量
3. **尋找 Juno 零結果的額外物理機制**（RQ4）——多極展開無法解釋，需要新思路
4. **JUICE 2026 年 9 月地球飛掠預測**——查詢精確軌道參數，密封預測 ΔV

## 信號強度的正確排序（2026-06-27 確立）

```
1. 幾何（主導）：P₂ 節點 ±54.7°     r=0.852，零自由參數
2. 太陽風（次要）：ap 指數修正       c₂=−0.249 mm/s/nT，二階效應
3. 三體潮汐（三階）：月球-太陽配置   RMS 改善 26%
```

## 已排除的問題（2026-06-27）

- **「7.3 倍放大機制」** ← 虛假問題，由體積積分（η=1）解決
- **太陽風截斷 plasmasphere** ← 計算排除（Lpp 始終在 B_main 以外）
- **電漿耦合解釋 B=394 km** ← 無任何電漿尺度對應

---

## 更新原則

- 每次新發現只更新**相關的單一檔案**，不重寫整個專案
- README 的「核心主張」在有重大框架升級時更新
- 05_Predictions.md 的預測內容**永不修改**（只添加驗證結果）
