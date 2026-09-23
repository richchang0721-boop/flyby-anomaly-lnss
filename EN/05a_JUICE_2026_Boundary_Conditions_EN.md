# 05a — JUICE 2026 Earth Flyby: Pre-registered Boundary Conditions

**Language: English | [繁體中文](../05a_JUICE_2026_Boundary_Conditions.md)**

> **Sealing statement**
> This document was committed **before** perigee (2026-09-28 11:46 TDB) and will not be modified afterward.
> All post-flyby analysis, results, and corrections go into a separate results document; this file is never rewritten.
> Commit hash: `[filled in via the README permalink after commit]`

---

## 1. Purpose

This document records the environmental state at the JUICE Earth flyby and declares in advance:

- which environmental variables will enter any later comparison;
- their role in the model and their fixed parameters;
- the interpretation rule for whether or not a residual appears.

The purpose is to **prevent post hoc variable selection**. Any factor introduced after the flyby is labeled *exploratory* and does not count as confirming evidence.

## 2. Relation to the sealed prediction

This document **does not modify** the sealed prediction in `05_Predictions.md`, which stands as:

| Item | Sealed value |
|---|---|
| δᵢ | −0.690° |
| δₒ | +4.385° |
| V∞ | 12.115 km/s |
| ΔV_P1 | +0.107 mm/s |
| \|P₂(cos δ_peri)\| | 0.9991 |
| Criterion | If \|ΔV\| > 1 mm/s → direct evidence for a P₂ component |

This document only supplements environmental conditions. It is an **auxiliary registration**, not a new prediction.

## 3. Flyby parameters

Source: `results.json` (produced by `reconstruct.py` from raw JPL Horizons files in `data/raw/`)

| Item | Value | Source |
|---|---|---|
| Perigee time | 2026-09-28 11:46 TDB | results.json |
| Perigee altitude | 8,645.5 km | results.json |
| Frame | Equatorial / ICRF, geocentric, 1-minute step | pipeline spec |

## 4. Sun–Earth–Moon geometry at perigee

The flyby occurs about 43 hours after full Moon. Near full Moon, Sun, Earth, and Moon are nearly collinear and the solar and lunar tidal gradients are nearly aligned (spring-tide configuration).

All values below were computed by `lunar_solar_geometry.py` from raw JPL Horizons files and are stored in `results.json` under the key `JUICE_2026_boundary_conditions` (computed 2026-09-23 04:19 UTC).

| Item | Value | Method |
|---|---|---|
| Most recent full Moon | 2026-09-26 16:50:48 TDB (≈ 16:49:39 UTC) | Geocentric geometric ecliptic longitude difference Moon (301) − Sun (10) = 180°, linear interpolation on 1-minute grid |
| Time from full Moon to perigee | +42.92 h (after full Moon) | from the above |
| Sun–Earth–Moon elongation (Sun–Moon angle seen from Earth) | 156.683° | angle between r_Sun and r_Moon |
| Lunar phase angle (Sun–Earth angle seen from Moon) | 23.261° | from vectors; sum with elongation = 179.944°, self-consistent |
| Lunar illuminated fraction | 0.9594 | (1 + cos phase angle) / 2 |
| Earth–Moon distance | 373,532.1 km | Horizons geocentric range |
| Angle: Moon direction vs. perigee position | 121.485° | angle between r_Moon and JUICE r_peri |
| Angle: Moon direction vs. perigee velocity | 147.917° | angle between r_Moon and v_peri |
| Angle: Sun direction vs. perigee position | 81.207° | angle between r_Sun and r_peri |
| Angle: Sun direction vs. perigee velocity | 8.861° | angle between r_Sun and v_peri |
| Lunar RA / Dec | 24.2886° / +14.867° | Horizons ICRF |
| Solar RA / Dec | 184.5928° / −1.9875° | Horizons ICRF |

**Geometric summary:** At perigee, JUICE is on the anti-lunar side of Earth (121° from the Moon direction), and its velocity points almost directly toward the Sun (8.9°).

**Cross-check:** Perigee time (2026-Sep-28 11:46 TDB), altitude (8,645.5 km), and speed (13.1233 km/s) match the sealed `reconstruct.py` reconstruction exactly, confirming the three input files share an aligned time grid.

**Horizons query specification** (identical to the JUICE query):
- Center: `500@399` (geocentric)
- Frame: ICRF, reference plane = equatorial (`REF_PLANE='FRAME'`)
- Step: 1 minute; Moon/Sun span 2026-09-24 00:00 to 2026-10-01 00:00 TDB (must include full Moon)
- JUICE raw file: `data/raw/Juice_horizons_results_min.txt`
- Moon/Sun raw files: `data/raw/Moon_2026Sep_horizons_geocentric.txt`, `data/raw/Sun_2026Sep_horizons_geocentric.txt`
- Note: Horizons defaults to the ecliptic plane and must be switched to equatorial for every query; long outputs saved from a browser may be truncated, so download with `curl`.

## 5. Pre-declared auxiliary terms

### 5.1 Standard third-body gravity (Sun, Moon)

Standard orbital-mechanics terms, assumed to be fully absorbed by conventional orbit determination (OD).
**This framework does not invoke lunar gravity itself as an explanation.** Full Moon is a geometric state, not an additional force.

Newtonian third-body tidal (differential) acceleration at the perigee instant, recorded for context only:

| Item | Value |
|---|---|
| Lunar tidal acceleration | 1.868 × 10⁻⁶ m/s² |
| Solar tidal acceleration | 6.12 × 10⁻⁷ m/s² |
| Total | 2.250 × 10⁻⁶ m/s² |
| Total, radial component | −7.37 × 10⁻⁷ m/s² |
| Total, along-velocity component | +2.116 × 10⁻⁶ m/s² |

**Interpretive limit:** These are instantaneous values. The along-track component changes sign over the flyby, so it must **not** be multiplied by a time span and compared as a net ΔV with the mm/s anomaly. These terms are fully modeled by conventional OD.
Constants used: GM_Moon = 4902.800118 km³/s², GM_Sun = 1.32712440041 × 10¹¹ km³/s² (to be verified against DE440 documentation and moved to `constants.py`).

### 5.2 Lunar–solar tidal term (tertiary signal in this framework)

- Prior result (`02_Constraints.md`, `04_Mathematics.md`): two-variable model `ΔV = 10.94 − 0.47·ap + 5.18×10¹³·T_proj`, RMS reduced from 3.99 to 2.94 mm/s (~26% improvement).
- **Status: not yet re-verified against corrected data.** The model was fit before the 2026-07-02 audit; the tidal projection T_proj alone correlates with ΔV at only r = +0.093; with n = 7 and two parameters, part of the 26% improvement may be overfitting.
- For this flyby the term is therefore recorded **as environment only** (see Section 4 and 5.1). **It yields no quantitative prediction and carries no evidential weight.**
- The model includes an intercept (10.94) and is a fit to total ΔV; it cannot be added as a correction on top of ΔV_P1.
- No coefficient may be refit using JUICE data after the flyby. Any future re-verification must first be done on historical flybys and recorded separately.

### 5.3 Geomagnetic activity (ap index, secondary signal in this framework)

- Prior result (`04_Mathematics.md`): `ΔV = 3.80 + 0.579·ΔV_Anderson − 0.249·ap`, c₂ = −0.249 mm/s/nT.
- **Status: pending re-verification.** The fit used pre-audit ΔV_Anderson values (Juno's P₁ has since been corrected from +10.4 to ~+6.0–6.3 mm/s), so the coefficient must be refit with corrected data. The model in 5.2 uses an ap coefficient of −0.47; the two have not been reconciled.
- This model also includes an intercept (3.80) and cannot be added as a correction on top of ΔV_P1. For this flyby ap is therefore **a recorded variable only, with no quantitative prediction**.
- **Selection rule (fixed in advance, consistent with the historical data in `01_Observations.md`):**
  - Source: NASA OMNIWeb, OMNI2 daily, ap index (https://omniweb.gsfc.nasa.gov/form/dx1.html)
  - Window: the daily value for the UTC day containing perigee (2026-09-28)
  - If OMNI2 has not yet been updated to that day at analysis time, status is "pending"; no other source or window may be substituted.
- After the flyby, no switch to another source or window (e.g. 3-hour ap, ±N-hour averages) is permitted.

### 5.4 Other geometric state

| Item | Value |
|---|---|
| Earth Rotation Angle at perigee (ERA) | 183.1372° |
| Greenwich Mean Sidereal Time at perigee (GMST, IAU 2006, UT1 ≈ UTC) | 183.4798° |
| B_main scale | 16,076 km (fixed parameter, not adjusted) |

## 6. Interpretation rule (fixed in advance)

Let R = the residual after conventional OD has removed all known Newtonian, GR, third-body, and non-gravitational perturbations.

| Case | Interpretation |
|---|---|
| No official residual or OD uncertainty published | Status "pending"; no inference from informal sources |
| \|R\| within OD uncertainty | No anomaly. Recorded as a constraint; the P₂ > 1 mm/s hypothesis fails for this flyby |
| \|R\| > 1 mm/s | Per the `05_Predictions.md` criterion, evidence for a P₂ component; the geometry and ap values recorded in Sections 4–5 are compared descriptively only (5.2 and 5.3 are not re-verified and are not tested quantitatively) |
| In between | Compare with ΔV_P1 = +0.107 mm/s and check sign consistency |

**Additional principles:**
1. If a residual exists, compare only against variables and directional relations declared in this document.
2. Any variable proposed after the flyby is labeled *exploratory* and recorded separately.
3. A null or non-matching result is recorded as a negative result in `CHANGELOG.md`.

## 7. Source notes and discrepancies

| Item | This repo (Horizons) | External source | Note |
|---|---|---|---|
| Perigee altitude | 8,645.5 km | ESA: "within 8640 km" | ESA value is rounded; difference ~5.5 km, consistent. This repo uses the Horizons value throughout |
| Perigee time | 11:46 TDB (≈ 11:44:50 UTC) | ESA: 11:45 UTC (13:45 CEST) | Consistent |
| Perigee location | — | ESA: over the Indian Ocean | Recorded only |

ESA source: *Juice to fly past Earth for third gravity assist*, published 2026-09-21, https://www.esa.int/Science_Exploration/Space_Science/Juice/Juice_to_fly_past_Earth_for_third_gravity_assist

The same article states that Juice's 10 science instruments will observe Earth and the Moon between 23 September and 3 October, and that the navigation camera will point toward the lunar horizon to test a new technique for improving optical-navigation accuracy.
This is recorded as context only and **has no bearing on this framework's prediction**.

## 8. What this document does not do

- It does not modify any sealed value in `05_Predictions.md`.
- It does not propose a new physical mechanism.
- It does not presume that full Moon produces an LNSS effect; full Moon is recorded only as an environmental state.
- It does not cite any value not produced by the pipeline (the ESA values in Section 7 are external side-by-side references only and enter no calculation).
