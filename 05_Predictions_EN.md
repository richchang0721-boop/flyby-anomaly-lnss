# 05 — Predictions (Sealed)

**Last updated:** 2026-06-28 v1.4  
**Sealed date:** 2026-06-28  
**Data source:** JPL Horizons (queried 2026-06-28)

> All predictions were written before observational results were available and will not be modified retroactively. Verification results may be appended after each flyby date.

---

## JUICE Earth Flyby (2024-08-20, completed)

| Parameter | Value |
|-----------|-------|
| Perigee altitude | 6,840 km (ESA confirmed) |
| V∞ | 6.4 km/s |
| δ_peri (estimated) | ≈ +62.5° |
| P₂(cosδ_peri) | −0.180 |

**Prediction:** No meaningful prediction possible.

At 6,840 km altitude, the field retains only exp(−6840/16076) ≈ 65% of its surface value. ESA reported no anomaly; the flyby was described as "flawless."

**Result: Consistent with framework (high altitude → weak effect; no anomaly reported)**

---

## JUICE Earth Flyby (2026-09-28/29) ★ Sealed Prediction ★

| Parameter | Value | Source |
|-----------|-------|--------|
| Flyby date | **2026-09-28/29** (confirmed by JPL data) | JPL Horizons |
| Perigee altitude | To be confirmed (6h-step data needed) | — |
| V∞ | **12.115 km/s** | JPL Horizons |
| δᵢ (inbound asymptote declination) | **−0.690°** | JPL Horizons (Sep-01 far field) |
| δₒ (outbound asymptote declination) | **+4.385°** | JPL Horizons (Oct-15 far field) |
| δ_peri (perigee declination) | **≈ +1.4°** (1-day step estimate) | JPL Horizons position |
| cosδᵢ − cosδₒ | **+0.002855** | Calculated |

**Data source:** JPL Horizons (queried 2026-06-28), JUICE NAIF ID: −28, Earth NAIF ID: 399, Ecliptic J2000, Solar System Barycenter. Trajectory based on tracking data through 2026-May-20; subsequent values are predicted.

---

### Velocity Direction Evolution (JUICE relative to Earth)

| Date | \|V∞\| (km/s) | Dec (°) | Note |
|------|--------------|---------|------|
| Aug-15 | 14.791 | +2.341 | Far inbound (still under Earth influence) |
| Sep-01 | 12.731 | −0.690 | **Inbound asymptote (stable)** |
| Sep-10 | 11.831 | −1.723 | Approaching flyby |
| Sep-28 | 10.992 | −2.236 | Last day before flyby |
| **Sep-29** | **10.990** | **+5.659** | **← Flyby! Velocity direction jump** |
| Oct-07 | 11.092 | +5.315 | Outbound stabilizing |
| Oct-15 | 11.498 | +4.385 | **Outbound asymptote (stable)** |

The near-conservation of \|V∞\| before and after (10.99 vs 11.50 km/s) confirms a hyperbolic flyby trajectory.

---

### Sealed Prediction (sealed 2026-06-28)

```
Anderson (P₁) term:
  ΔV_P1 = V∞ × K × (cosδᵢ − cosδₒ)
         = 12.115 km/s × 3.097×10⁻⁶ × 0.002855
         = +0.107 mm/s

Geometric analysis:
  δᵢ ≈ −0.7°, δₒ ≈ +4.4° (difference: 5.1°, both at low latitude)
  → P₁ path integral nearly vanishes; Anderson main term almost cancels

P₂ component:
  δ_peri ≈ +1.4° (near equator)
  |P₂(cosδ_peri)| = 0.9991 (very close to maximum value of 1)
  → P₂ field strength near maximum at perigee
  → If P₂ term exists, effect may reach 1–3 mm/s
```

**Final sealed prediction:**

```
★ If only P₁ (pure Anderson formula):
  ΔV ≈ +0.11 mm/s  (below detection threshold)

★ If P₂ component exists (LNSS framework):
  |ΔV| ≈ 1–3 mm/s  (P₂-dominated)

Decision criteria:
  |ΔV| < 0.5 mm/s  →  supports pure Anderson (P₁ only)
  |ΔV| > 1.0 mm/s  →  supports existence of P₂ component
  |ΔV| > 3.0 mm/s  →  outside all framework parameters; theory revision needed
```

**This flyby is the critical test for the P₂ component. Since P₁ ≈ 0, any anomaly > 1 mm/s directly points to P₂ contribution.**

**Confidence: Medium (δᵢ and δₒ are precise; A₂ coefficient unknown)**

★ **Sealed: 2026-06-28** | Revealed: after 2026-09-28/29 flyby |

---

## Europa Clipper Earth Flyby (2026-12-03) ★ Sealed Prediction ★

| Parameter | Value | Source |
|-----------|-------|--------|
| Flyby date | **2026-12-03** (confirmed) | NASA JPL |
| Perigee altitude | ~3,200 km (official); Horizons predicted trajectory pending confirmation | NASA |
| V∞ | **11.596 km/s** | JPL Horizons |
| δᵢ (inbound asymptote declination) | **+29.34°** | JPL Horizons |
| δₒ (outbound asymptote declination) | **+30.61°** | JPL Horizons |
| δ_peri (perigee declination) | **≈ −30.4°** (estimated) | JPL Horizons position |
| cosδᵢ − cosδₒ | **+0.01105** | Calculated |

**Data source:** JPL Horizons (queried 2026-06-28), Europa Clipper NAIF ID: −159, Earth NAIF ID: 399. Relative velocity = spacecraft velocity − Earth velocity (Ecliptic J2000, Solar System Barycenter).

**Note:** Trajectory segment after 2026-09-19 uses pre-launch prediction (V7). Tracking data through 2026-May-19 confirms V∞ direction; asymptote declinations are reliable.

---

### Sealed Prediction (sealed 2026-06-28)

```
Anderson (P₁) term:
  ΔV_P1 = V∞ × K × (cosδᵢ − cosδₒ)
         = 11.596 km/s × 3.097×10⁻⁶ × 0.01105
         = +0.397 mm/s

Geometric analysis:
  δᵢ ≈ δₒ (difference: 1.27°) → P₁ path integral nearly cancels
  Nearly symmetric flyby (inbound from ~29°N, outbound toward ~31°N)

P₂ correction term:
  |P₂(cosδ_peri)| = |P₂(cos(−30.4°))| = 0.616  (>> threshold 0.06)
  → Framework predicts nonzero P₂ correction; coefficient A₂ unknown
  → Estimated P₂ contribution: ±1–2 mm/s (high uncertainty)
```

**Final sealed prediction:**

```
★ |ΔV| < 2 mm/s

  P₁ main term:  ≈ +0.40 mm/s  (precise)
  P₂ correction: ±1–2 mm/s     (uncertain)
  Overall:       |ΔV| < 2 mm/s  (low confidence)

If pure Anderson (P₁ only):      ΔV ≈ +0.40 mm/s
If P₂ contributes (A₂ unknown):  |ΔV| up to ~2 mm/s
```

**Falsification condition:** If |ΔV| > 3 mm/s is observed, this falls outside all parameter combinations of the framework and requires theory revision.

**Confidence: Low (P₁ term precise; flyby geometry nearly symmetric; P₂ term uncertain)**

★ **Sealed: 2026-06-28** | Revealed: after 2026-12-03 flyby |

---

## Threshold Hypothesis — General Prediction

### Definition

**|P₂(cosδ_peri)| = 0.06** is the estimated boundary between null and anomalous flybys.

Corresponding "calm zone" declination range: **52.3° to 57.2°** (centered on ±54.7°, width ≈ 5°)

### Physical Interpretation (corrected 2026-06-28)

|P₂(cosδ_peri)| is a **proxy for orbital symmetry**, not a direct measure of field strength at perigee. The variable δ_peri does not directly enter the path integral — both the Anderson formula and the P₂ path integral depend only on δᵢ and δₒ. When perigee falls near ±54.7°, the inbound and outbound trajectory segments become nearly mirror-symmetric, causing the P₂ path integral to vanish.

### General Sealed Prediction

| Perigee declination δ_peri | \|P₂(cosδ_peri)\| | Prediction | Condition |
|---------------------------|-------------------|------------|-----------|
| 52.3° to 57.2° (or −57.2° to −52.3°) | < 0.06 | **\|ΔV\| < 0.5 mm/s (unobservable)** | High-precision tracking |
| Other latitudes | > 0.06 | **\|ΔV\| ≈ 19.3 × \|P₂\| mm/s** | High-precision tracking |

### Linear Relationship

```
|ΔV| ≈ 19.3 × |P₂(cosδ_peri)|  mm/s    (when |P₂| > 0.06)
r = 0.852  (n = 7)
```

### Confidence Assessment

**Classification accuracy: 7/7 = 100%** (on historical data)

**Honest limitations:**
- n = 7; a single new flyby could shift the gap estimate (currently 0.036 < |P₂|_c < 0.091)
- This is more likely a "continuous field strength below detection threshold" than a phase transition
- The theoretical |P₂|_c should be 0 (exact P₂ node); the observed 0.06 reflects finite tracking precision

**Confidence: Low (n = 7; more flybys required)**

---

## Key Prediction Summary (2026-06-28 version)

| Scenario | Perigee latitude | \|P₂\| | Prediction | Confidence |
|----------|-----------------|--------|------------|------------|
| In calm zone (52°–57°) | Any | < 0.06 | \|ΔV\| ≈ 0 | Low (n=7) |
| Low latitude (< 40°) | Any | > 0.3 | \|ΔV\| ≈ 5–10 mm/s | Low |
| Juno-like scenario | 53.5° | 0.031 | \|ΔV\| ≈ 0 | Medium |
| Cassini-like scenario | 58.5° | 0.091 | \|ΔV\| ≈ 2 mm/s | Medium |

---

## Timestamp

All predictions in this document were sealed on **2026-06-28**, prior to any observational results from the 2026 flybys. Only verification results may be appended; prediction content is immutable.
