# 01 — Observational Data

**Last updated:** 2026-06-28 v1.4

---

## Flyby Data (Coherent Doppler Tracking)

| Flyby | Date | ΔV observed | δᵢ | δₒ | V∞ (km/s) | Perigee alt. | δ_peri (est.) |
|-------|------|-------------|-----|-----|-----------|-------------|---------------|
| Galileo I | 1990-12-08 | +3.92 mm/s | −12.52° | +34.26° | 8.949 | 960 km | −61.8° |
| Galileo II | 1992-12-08 | −4.60 mm/s | −34.26° | −4.50° | 8.877 | 303 km | +74.2° |
| NEAR | 1998-01-23 | +13.46 mm/s | −20.76° | +72.03° | 6.851 | 539 km | −32.5° |
| Cassini | 1999-08-18 | −2.00 mm/s | −12.92° | −4.99° | 16.010 | 1,172 km | +58.5° |
| Rosetta I | 2005-03-04 | +1.82 mm/s | −2.81° | +34.29° | 3.863 | 1,954 km | −71.4° |
| Messenger | 2005-08-02 | +0.02 mm/s ≈ 0 | +31.44° | −31.92° | 4.056 | 2,347 km | +53.3° |
| **Juno** | **2013-10-09** | **0.00 mm/s** | **−2.00°** | **−48.90°** | **9.820** | **561 km** | **+53.5°** |
| **OSIRIS-REx** | **2017-09-22** | **< 0.1 mm/s (upper limit)** | TBD | TBD | 5.4* | **17,237 km** | TBD |

\* V∞ shown is the launch escape velocity; the actual flyby value requires confirmation from precise trajectory data.

**Significance of OSIRIS-REx (added 2026-07-01):** Perigee altitude of 17,237 km falls just outside the framework's derived B_main = 16,076 km (see 04_Mathematics_EN.md) — the only observed flyby with an altitude exceeding B_main. The framework predicts ~34% field retention at this altitude (exp(−17237/16076)); the observed <0.1 mm/s upper limit is consistent with this, but the signal is too weak and δ_in/δ_out have not yet been obtained, so this cannot serve as a strong test — recorded as a candidate boundary case.

**Difference from the other seven cases:** OSIRIS-REx has not yet been analyzed with the same detail as the other seven cases (δ_peri, P₂ not computed). It is included for data completeness; the |P₂|_c classification accuracy (7/7) still refers to the original seven cases and does not include this one.

**Excluded cases (non-coherent tracking):**
Rosetta II (2007), Rosetta III (2009), EPOXI (2008): insufficient tracking precision to detect mm/s deviations — instrument limitation, not physical null result.

---

## Planetary Distances at Each Flyby

| Flyby | Moon (LD) | Venus (AU) | Jupiter (AU) | Saturn (AU) |
|-------|-----------|------------|--------------|-------------|
| Galileo I | 1.002 | 1.683 | 4.67 | 10.77 |
| Galileo II | 0.992 | 0.990 | 5.77 | 10.37 |
| NEAR | 1.021 | **0.275** | 5.90 | 9.62 |
| Cassini | 1.046 | **0.289** | 4.52 | 9.02 |
| Rosetta I | 0.961 | 1.704 | 4.60 | 8.44 |
| Juno | 0.963 | 0.839 | 5.11 | 10.76 |

Venus distance varies by 520% across flybys — the largest external variable.

---

## Solar Activity (NASA OMNIWeb precise daily values, queried 2026-06-27)

Source: https://omniweb.gsfc.nasa.gov/form/dx1.html — OMNI2 daily, ap index + F10.7 index

| Flyby | Date | ap (nT) | F10.7 (sfu) | Solar cycle position |
|-------|------|---------|-------------|----------------------|
| Galileo I | 1990-12-08 | 8 | **223.6** ← highest | Cycle 22 just past maximum |
| Galileo II | 1992-12-08 | 26 | 124.8 | Cycle 22 declining |
| NEAR | 1998-01-23 | **4** ← low | 93.9 | 17 months after Cycle 23 minimum |
| Cassini | 1999-08-18 | 28 | 133.9 | Cycle 23 rising |
| Rosetta I | 2005-03-04 | **2** ← lowest | **77.7** ← lowest | Cycle 23 late decline |
| **Juno** | **2013-10-09** | **29** ← highest | 113.1 | Cycle 24 pre-maximum |

### Correlation Analysis

| Feature | r vs \|dV\| | r vs dV | Note |
|---------|------------|---------|------|
| F10.7 | −0.14 | −0.11 | **Weak** — background solar activity (weekly/monthly scale) |
| **ap** | **−0.50** | **−0.72** | **Strong** — instantaneous geomagnetic activity (solar wind compression) |

### Key Finding

**ap (geomagnetic activity index) is a better predictor of flyby anomaly magnitude than F10.7.**

- Juno (ap = 29, highest) → dV = 0
- NEAR (ap = 4, near lowest) → dV = +13.46 (largest anomaly)
- Rosetta I (ap = 2, lowest) → dV = +1.82

**Updated interpretation (2026-06-28):** The ap–dV correlation (r = −0.72) is partly a confound effect. Juno simultaneously has high ap (29) and low |P₂(cosδ_peri)| (0.031). The true primary driver is orbital geometry (|P₂|); ap is a secondary modifier with coefficient c₂ = −0.249 mm/s/nT.

---

## Data Quality Notes

- Anderson formula prediction accuracy for 5 anomalous cases: residuals within ±1 mm/s
- Juno residual: −10.4 mm/s — the largest of all cases (open problem RQ4)
- Messenger's null result is partly geometric (δᵢ ≈ −δₒ, near-symmetric orbit), not identical in origin to Juno's null result
