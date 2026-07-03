# 01 — Observational Data

**Last updated:** 2026-07-02 v1.6 (all 7 historical flyby angles reconstructed via JPL Horizons, replacing original estimates)

---

## ✅ 2026-07-02 Update: δ_peri audit resolved, all 7 flybys reconstructed

The previous audit warning (δ_peri definition conflict, Juno angle outlier) has been resolved via full reconstruction: JPL Horizons, equatorial frame (ICRF), 1-minute-step precise perigee search, both position and velocity declination computed. Full verdict and per-case verification in 07_Open_Problems_EN.md, "Complete Reconstruction of All 7 Historical Flybys."

**Core conclusions:**
- δᵢ, δₒ (asymptote declinations): 6/7 cases match old values well (including sign flips that don't affect cosine values). Only **Juno's δᵢ, δₒ themselves were wrong** — new values match independent literature (Jouannic 2015, Acedo 2017) almost exactly.
- δ_peri (perigee declination): **old values are wrong for all 7 cases**, and in the systematic Candidate 7 criterion test, δ_peri contributed zero correct classifications — this column should be retired from further analysis.
- Perigee altitudes: reconstructed values match official altitudes to within <25km (mostly <10km) across all 7 cases, validating the method.

The table below shows old and new values side by side; **new values supersede old ones as the official dataset.**

---

## Flyby Data (Coherent Doppler Tracking) — Reconstructed via JPL Horizons (2026-07-02)

| Flyby | Date | ΔV observed | δᵢ (new) | δₒ (new) | δ_peri (position, new) | δ_peri (velocity, new) | V∞ (km/s) | Perigee alt. (precise) |
|-------|------|-------------|----------|----------|------------------------|-------------------------|-----------|--------------------------|
| Galileo I | 1990-12-08 | +3.92 mm/s | −12.5° | −34.0° | +23.81° | −25.58° | 8.949 | 970.58 km |
| Galileo II | 1992-12-08 | −4.60 mm/s | −34.25° | −4.90° | −32.45° | −21.55° | 8.877 | 309.62 km |
| NEAR | 1998-01-23 | +13.46 mm/s | −20.58° | −72.00° | +32.84° | −51.33° | 6.851 | 539.63 km |
| Cassini | 1999-08-18 | −2.00 mm/s* | −12.92° | −5.48° | −22.73° | −9.32° | 16.010 | 1,196.78 km |
| Rosetta I | 2005-03-04 | +1.82 mm/s | −2.0°† | −34.04° | +20.83° | −27.13° | 3.863 | 1,962.71 km |
| Messenger | 2005-08-02 | +0.02 mm/s ≈ 0 | +32.2° | −32.91° | +46.92° | −0.04° | 4.056 | 2,343.75 km |
| **Juno** | **2013-10-09** | **0.00 mm/s** | **+14.16°**‡ | **+39.40°**‡ | **−32.22°** | **+28.57°** | **9.820** | **570.82 km** |
| **OSIRIS-REx** | **2017-09-22** | **< 0.1 mm/s (upper limit)** | TBD | TBD | 5.4** | **17,237 km** | TBD |

\* Cassini's observed value is disputed in the literature: Anderson 2008 gives −2.00 mm/s; later compilations (Jouannic et al.) give −0.5±0.5 mm/s — unresolved.

† Rosetta I's δᵢ has lower precision than other cases: this flyby's low V∞ (3.86 km/s) means the asymptote converges more slowly, and it had not fully stabilized within the query window.

‡ **Juno's δᵢ, δₒ are completely different from the old database values** (−2.00°, −48.90°), but closely match independent literature (Jouannic et al. 2015: +14.17°/+39.50°; Acedo 2017: −14.308°/+39.409°). The new values are judged reliable; the old database values were in error.

\*\* OSIRIS-REx V∞ shown is the launch escape velocity; the actual flyby value requires confirmation from precise trajectory data.

### Old Values (retained for traceability; no longer used as official data)

| Flyby | δᵢ (old) | δₒ (old) | δ_peri (old) |
|-------|----------|----------|---------------|
| Galileo I | −12.52° | +34.26° | −61.8° |
| Galileo II | −34.26° | −4.50° | +74.2° |
| NEAR | −20.76° | +72.03° | −32.5° |
| Cassini | −12.92° | −4.99° | +58.5° |
| Rosetta I | −2.81° | +34.29° | −71.4° |
| Messenger | +31.44° | −31.92° | +53.3° |
| Juno | −2.00° | −48.90° | +53.5° |

**Observed pattern:** δₒ shows a recurring "same magnitude, flipped sign" discrepancy (Galileo I, NEAR, Rosetta I), suggesting a possible systematic sign-convention issue in how the old database computed outbound-leg angles. δᵢ is largely reliable except for Juno. δ_peri is unreliable across the board, and no computation method for it was ever documented in any project file.

**Significance of OSIRIS-REx (added 2026-07-01):** Perigee altitude of 17,237 km falls just outside the framework's derived B_main = 16,076 km (see 04_Mathematics_EN.md) — the only observed flyby with an altitude exceeding B_main. The framework predicts ~34% field retention at this altitude (exp(−17237/16076)); the observed <0.1 mm/s upper limit is consistent with this, but the signal is too weak and δᵢ/δₒ have not yet been obtained, so this cannot serve as a strong test.

**Excluded cases (non-coherent tracking):**
Rosetta II (2007), Rosetta III (2009), EPOXI (2008): insufficient tracking precision to detect mm/s deviations — instrument limitation, not physical null result. (To do: Jouannic 2015 and Acedo 2017 provide angles and observed values for these cases — see action items in 07_Open_Problems_EN.md.)

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
|-------|------|---------|-------------|-----------------------|
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

⚠️ **Note (2026-07-02):** This correlation analysis, and the physical interpretation below ("Juno's ap=29 may have compressed the LNSS band"), were partly framed around the old |P₂(cosδ_peri)| narrative. RQ13 already established ap as a secondary modifier, and the new δ_peri-based κ_i vs ap discriminating test (see 07_Open_Problems_EN.md, RQ12) supports "κ is an intrinsic background-field constant, not modulated by the local space environment." The raw ap–dV correlation numbers (pure observational statistics, not δ_peri-dependent) remain valid; the physical interpretation below should be re-examined.

### Key Finding

**ap (geomagnetic activity index) is a better predictor of flyby anomaly magnitude than F10.7.**

- Juno (ap = 29, highest) → dV = 0
- NEAR (ap = 4, near lowest) → dV = +13.46 (largest anomaly)
- Rosetta I (ap = 2, lowest) → dV = +1.82

**Physical interpretation (pending re-examination, see note above):** ap directly measures the instantaneous solar wind compression of Earth's magnetic field.

---

## Data Quality Notes

- Anderson formula prediction accuracy with the new angles (re-verified 2026-07-02): Galileo I/II, NEAR, Messenger errors <0.2 mm/s; Rosetta I ~0.2mm/s; Cassini ~1mm/s (but the observed value itself is disputed in the literature); **Juno now predicts +5.99~6.34 mm/s (not the old 10.4 mm/s), closely matching Acedo (2017)'s independently computed 6.3355 mm/s**
- Juno's residual is now corrected to approximately **−6.0 to 6.3 mm/s** (the previously recorded −10.4 mm/s was computed from erroneous angles and has been corrected)
- Messenger's null result comes from geometric symmetry in the orbit design (δᵢ ≈ −δₒ; the new angles show even better symmetry than the old ones: 32.2° vs 32.91°), not identical in origin to Juno's null result
