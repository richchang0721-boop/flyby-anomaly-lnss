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

The flyby occurs close to full Moon (roughly two days after). Near full Moon, Sun, Earth, and Moon are nearly collinear and the solar and lunar tidal gradients are aligned (spring-tide configuration).

The values below **must be computed by the pipeline**. They may not be estimated in prose or taken from LLM output.

| Item | Value | Method |
|---|---|---|
| Most recent full Moon | `[results.json]` | Horizons: geocentric ecliptic longitude difference Moon (301) − Sun (10) = 180° |
| Time from full Moon to perigee | `[results.json]` | from the above |
| Sun–Earth–Moon phase angle | `[results.json]` | angle between geocentric r_Sun and r_Moon |
| Lunar illuminated fraction | `[results.json]` | from phase angle |
| Earth–Moon distance | `[results.json]` | Horizons geocentric range |
| Angle: Moon direction vs. perigee position | `[results.json]` | angle between r_Moon and JUICE r_peri |
| Angle: Moon direction vs. perigee velocity | `[results.json]` | angle between r_Moon and v_peri |
| Lunar declination | `[results.json]` | Horizons |
| Solar declination | `[results.json]` | Horizons |

**Horizons query specification** (identical to the JUICE query):
- Center: `500@399` (geocentric)
- Frame: ICRF / equatorial
- Step: 1 minute, spanning ±24 h around perigee
- Raw files: `data/raw/Moon_2026Sep_horizons_geocentric.txt`, `data/raw/Sun_2026Sep_horizons_geocentric.txt`

## 5. Pre-declared auxiliary terms

### 5.1 Standard third-body gravity (Sun, Moon)

Standard orbital-mechanics terms, assumed to be fully absorbed by conventional orbit determination (OD).
**This framework does not invoke lunar gravity itself as an explanation.** Full Moon is a geometric state, not an additional force.

### 5.2 Lunar–solar tidal term (tertiary signal in this framework)

- Prior result: including the lunar–solar tidal term improved RMS by ~26%.
- **Status: `[to fill: re-verified against corrected results.json / not yet re-verified]`**
- If not re-verified, this term is recorded **as environment only** and carries no evidential weight.
- If re-verified, the expected correction is fixed here:
  - Sign: `[ ]`
  - Magnitude: `[ ] mm/s`
  - Formula and parameters: `[link to the relevant section of 04_Mathematics.md]`
- No coefficient of this term may be refit after the flyby.

### 5.3 Geomagnetic activity (ap index, secondary signal in this framework)

- Coefficient fixed: c₂ = −0.249 mm/s/nT (not to be adjusted)
- Data source: `[GFZ Potsdam definitive / nowcast — choose one and fix]`
- Time window: `[e.g. 3-hour ap values within ±3 h of perigee / daily Ap — choose one and fix]`
- ap values become available only after the flyby, but **the selection rule is fixed here in advance**.

### 5.4 Other geometric state

| Item | Value |
|---|---|
| Earth rotation phase at perigee (GMST) | `[results.json]` |
| B_main scale | 16,076 km (fixed parameter, not adjusted) |

## 6. Interpretation rule (fixed in advance)

Let R = the residual after conventional OD has removed all known Newtonian, GR, third-body, and non-gravitational perturbations.

| Case | Interpretation |
|---|---|
| No official residual or OD uncertainty published | Status "pending"; no inference from informal sources |
| \|R\| within OD uncertainty | No anomaly. Recorded as a constraint; the P₂ > 1 mm/s hypothesis fails for this flyby |
| \|R\| > 1 mm/s | Per the `05_Predictions.md` criterion, evidence for a P₂ component; then compare tidal and ap terms using the settings fixed in Section 5 |
| In between | Compare with ΔV_P1 = +0.107 mm/s and check sign consistency |

**Additional principles:**
1. If a residual exists, compare only against variables and directional relations declared in this document.
2. Any variable proposed after the flyby is labeled *exploratory* and recorded separately.
3. A null or non-matching result is recorded as a negative result in `CHANGELOG.md`.

## 7. Source notes and discrepancies

| Item | This repo (Horizons) | External source | Note |
|---|---|---|---|
| Perigee altitude / distance | 8,645.5 km | ESA public information: `[verify from original page]` km | Possibly a different trajectory solution or altitude definition; listed side by side, not mixed |
| Perigee time | 11:46 TDB | ESA: ~11:45 UTC | TDB − UTC ≈ 69 s; consistent |

ESA has stated that during the flyby period (approx. 23 Sep – 3 Oct) it will observe Earth and the Moon and conduct optical-navigation tests (`[link to original ESA page]`).
This is recorded as context only and **has no bearing on this framework's prediction**.

## 8. What this document does not do

- It does not modify any sealed value in `05_Predictions.md`.
- It does not propose a new physical mechanism.
- It does not presume that full Moon produces an LNSS effect; full Moon is recorded only as an environmental state.
- It does not cite any value not produced by the pipeline.
