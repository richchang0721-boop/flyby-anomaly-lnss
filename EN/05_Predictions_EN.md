# 05 — Predictions (Sealed)

**Last updated:** 2026-07-03 v1.8 (added post-seal validity notice)
**Sealed date:** 2026-06-28
**Data source:** JPL Horizons (queried 2026-06-28)

---

## ⚠️ Post-seal Validity Notice (added 2026-07-03)

**No sealed value below has been, or will be, modified — this is the core of the sealing principle and is not negotiable.**

But in the interest of honest disclosure: the **assumptions underlying** some sealed predictions below have since been overturned or downgraded by later research:

| Sealed content | Underlying assumption | Current status of assumption |
|-----------------|------------------------|-------------------------------|
| Candidate 7 topological criterion's prediction for JUICE (\|ΔV\|≈0) | Whether δ_peri crossing the 54.7356° node correctly classifies flybys | **Overturned** (2026-07-02; see 07_Open_Problems_EN.md — δ_peri contributed zero correct classifications across all 7 historical cases) |
| \|P₂(cosδ_peri)\| criterion's predictions for JUICE and Europa Clipper | The |P₂(cosδ_peri)| vs \|ΔV\| correlation, r=0.852 | **Overturned** (2026-07-02; reconstruction gives r=0.082 or −0.863, inconsistent in direction with the original claim) |
| P₃ correction term prediction | GEM-framework magnitude estimate | **Confidence upgraded** (2026-07-03, from pure speculation to a theoretically grounded estimate — see 07_Open_Problems_EN.md) |

**What this means:** if the actual JUICE or Europa Clipper flyby matches the Candidate-7 or |P₂| sealed predictions, **this cannot be taken as validation of those criteria themselves** — the historical data foundation those criteria were built on is known to be compromised. Both sealed predictions remain valid and will still be checked against observation (the sealing principle requires this), but the **interpretation** of the outcome must account for this contamination, and a correct match should not be used to vindicate Candidate 7 or the original |P₂| criterion.

---

## Coordinate Frame Audit Record (raised 2026-07-02 → resolved 2026-07-03)

All sealed values below are **unchanged** — the sealing principle does not permit retroactive adjustment. Process record:

**2026-07-02 audit warning:** This document records the Horizons queries as using "Ecliptic J2000" (see data source notes below), but the Anderson formula's δ requires **equatorial declination** (symmetry axis = Earth's rotation axis, not the orbital plane). The two frames differ by Earth's obliquity, 23.44°. JUICE's three characteristic angles are all single-digit (−0.69°, +1.4°, +4.385°) — an error of this magnitude could flip the "near the P₂ node" vs. "far from the node" classification entirely. Flagged as highest priority, to be resolved before the flyby.

**2026-07-03 resolution:**

- **JUICE: fully resolved.** The user re-queried Horizons with an explicitly specified equatorial reference plane (ICRF, "x-y axes of reference frame equatorial"). Result: δᵢ=−0.690°, δₒ=+4.385°, **matching the sealed values in this document exactly** (see 07_Open_Problems_EN.md, results.json). The original query, despite being labeled "Ecliptic J2000" in the write-up, was already outputting equatorial-frame values — this was a documentation labeling error, not a computational one. **The sealed prediction stands unchanged; no re-sealing needed.**
- **Europa Clipper: partially confirmed.** Using the same method over the query window (2026-11-03 to 2027-01-03), the window endpoints give δᵢ≈26.75°→29.34° and δₒ≈29.36°→30.61° in trend, matching sign and magnitude with the sealed values — no sign of a coordinate-frame error. However, the window endpoints are not true converged asymptotic points (the same pitfall JUICE's early estimate ran into), so a fully rigorous confirmation would require locating a clearly stable asymptotic plateau, as was done for JUICE. The perigee/δ_peri portion has already been precisely verified via 1-minute-step reconstruction (see 07_Open_Problems_EN.md); only the δᵢ/δₒ asymptotic convergence precision remains to be tightened — medium priority (the coordinate-frame-correctness evidence itself is already sufficient).

**Status:** JUICE closed; Europa Clipper pending a precise asymptote query | **Priority: Medium (no longer blocks prediction validity)**

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

### ★★★ Independent Supplementary Sealed Prediction (Candidate 7: Topological Classification, sealed 2026-07-01) ★★★

> **Important note: this section is an independent prediction added after the original sealed prediction above (2026-06-28); it does not modify or override the original content.** Both predictions use different criterion logic and both achieve 7/7 classification accuracy on the n=7 historical dataset, but they give **opposite** conclusions for JUICE 2026 — this is precisely why the framework deliberately retains both, letting observation adjudicate.

**Criterion logic (see 07_Open_Problems_EN.md, Candidate 7):** Whether any of the trajectory's three characteristic angles (δᵢ, δ_peri, δₒ) ever has an absolute value exceeding P₂'s exact node at 54.7356° (zero free parameters, not a fitted value).

**JUICE 2026-09-28/29's three angles:**
```
δᵢ = −0.690°,  δ_peri ≈ +1.4°,  δₒ = +4.385°
max(|δᵢ|, |δ_peri|, |δₒ|) = 4.385°  ≪  54.7356° (the node)
```

**The topological criterion's sealed prediction:**

```
All three angles fall within the equatorial band (never approach the node)
→ Classification: same class as Juno and Messenger (the two historical null results)
→ Prediction: |ΔV| ≈ 0 (should be a null result, even though |P₂(cosδ_peri)|=0.9991 is large)
```

**Direct comparison with the original sealed prediction (based on |P₂(cosδ_peri)|):**

| Criterion | Basis | JUICE prediction |
|-----------|-------|--------------------|
| \|P₂(cosδ_peri)\| criterion (original sealed prediction, RQ14) | δ_peri near equator, large P₂ value (0.9991) | If P₂ term exists, possible 1–3 mm/s anomaly |
| **Topological criterion (this section, Candidate 7)** | **All three angles far from the node (54.7°)** | **Null result, |ΔV| ≈ 0** |

**This is the first opportunity to observationally distinguish these two criteria.** Both perform identically on the n=7 historical dataset (7/7 each), purely a coincidence of an underdetermined model; the actual JUICE 2026-09 observation will directly tell us which one (or neither) reflects the true physical mechanism.

**Confidence: Medium (historical classification perfect with zero free parameters, but mechanism unknown, and directly contradicts the other sealed criterion)**

★ **Sealed: 2026-07-01** | Revealed: after the 2026-09-28/29 flyby, verified simultaneously with the original prediction above |

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

## P₃ Correction Term (any future flyby)

If the Helmholtz framework is correct, the l=3 P₃(cosδ) node is at ±39.2°.

**2026-07-03 update: this hypothesis now has its first theoretical magnitude backing** (see 07_Open_Problems_EN.md, "GEM derivation establishes A₂=0"). Using the GEM spin-octupole formula (Iorio 2019, MNRAS, citing Panhans & Soffel 2014), the A₃/A₁ amplitude ratio is estimated at roughly 1/300 to 1/2000, giving a P₃ magnitude estimate of **0.01–0.05 mm/s** — consistent in direction with the "very low confidence" assessment below, but now backed by a GR-derived order-of-magnitude estimate rather than pure intuition. A sealed-prediction-quality number requires further derivation (the boundary-term integral has not yet been completed — see the honest confidence notes in 07_Open_Problems_EN.md).

**Prediction:** A flyby with perigee near ±39.2° should show a smaller residual correction beyond the pure Anderson formula.

This requires high-precision tracking and a precise gravity model to detect (expected effect << 1 mm/s; current theoretical estimate: 0.01–0.05 mm/s).

**Confidence: Low (previously "very low"; upgraded slightly on 2026-07-03 due to GEM-theoretical magnitude support; still requires a dedicated mission to test observationally)**

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
