**[English](README.md) | [中文](README_ZH.md)**
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
velocity discrepancies observed in hyperbolic spacecraft trajectories past Earth,
absent in closed orbits. This repository develops the **LNSS (Local Nonlinear
Spatial Structure) / Perturbation Model** framework to explain these anomalies
using a gravitational perturbation field grounded in General Relativity.

---

## Key Results

| Finding | Status | Confidence |
|---------|--------|------------|
| Closed orbits: ΔV ≡ 0 (topological theorem) | ✓ Proven | ★★★★★ |
| Volume integral η = 1 (no amplification needed) | ✓ Confirmed | ★★★★☆ |
| Factor of 2 = two-way Doppler tracking | ✓ Candidate | ★★★☆☆ |
| Primary driver: \|P₂(cosδ_peri)\| (orbital symmetry) | ✓ Confirmed | ★★☆☆☆ |
| Threshold: \|P₂\|_c ≈ 0.06 (7/7 classification) | ✓ Empirical | ★★☆☆☆ |
| ap index: secondary modifier (c₂ = −0.249 mm/s/nT) | ✓ Confirmed | ★★☆☆☆ |
| Background field wavenumber κ = 1/16,076 km | Open (RQ12) | — |
| Juno zero result: additional mechanism needed | Open (RQ4) | — |

---

## Theoretical Framework

### The Anderson Formula

```
ΔV = V∞ · (2ωR/c) · (cosδᵢ − cosδₒ)
K = 2ωR/c = 3.097 × 10⁻⁶
```

### Why Closed Orbits Are Unaffected

For any closed orbit, δᵢ = δₒ (start = end point), therefore:

```
ΔV = V∞ · K · (cosδᵢ − cosδᵢ) = 0  (exact, topological)
```

This explains why ISS, GPS, Starlink, and all satellites show no anomaly — without any free parameters.

### The Factor of 2

Anderson et al. used **two-way Doppler tracking**: signal travels Ground → Spacecraft → Ground. Each leg experiences the Lense-Thirring metric perturbation once, doubling the effect:

```
Single-way: ΔV = (ωR/c) · (cosδᵢ − cosδₒ)
Two-way:    ΔV = 2·(ωR/c) · (cosδᵢ − cosδₒ)  ← Anderson formula
```

The factor of 2 is a property of the measurement method, not the field equation.

### The Perturbation Model

Earth disturbs a pre-existing background field Ψ_bg rather than generating LNSS from scratch:

```
Background field Ψ_bg  (wavenumber κ = 1/B_main, origin unknown)
        ↓  Earth mass + rotation → local perturbation
        ↓  Forms P₁/P₂ local modes (sinθ structure from GR)
        ↓  Solar wind (ap) modifies amplitude (secondary)
        ↓  Flyby anomaly ΔV
```

**Characteristic length:** B_main = 16,076 km = 2.52 R_E  
(determined by matching the Anderson coefficient via volume integral)

---

## Signal Hierarchy

```
1. Geometry (dominant):  P₂ node at ±54.7°    r = 0.852, zero free parameters
2. Solar wind (secondary): ap index             c₂ = −0.249 mm/s/nT
3. Tidal (tertiary):     Moon-Sun configuration  26% RMS improvement
```

### Threshold Prediction

| Condition | Prediction |
|-----------|------------|
| \|P₂(cosδ_peri)\| < 0.06 (perigee within ±52°–57°) | \|ΔV\| < 0.5 mm/s (unobservable) |
| \|P₂(cosδ_peri)\| > 0.06 (other latitudes) | \|ΔV\| ≈ 19.3 × \|P₂\| mm/s |

Classification accuracy: **7/7** on historical flybys (n=7, requires more data).

---

## Sealed Predictions (recorded 2026-06-28)

Both predictions use precise JPL Horizons trajectory data (queried 2026-06-28).

### JUICE Earth Flyby — 2026-09-28/29

| Parameter | Value | Source |
|-----------|-------|--------|
| δᵢ (inbound asymptote) | **−0.690°** | JPL Horizons (NAIF: −28) |
| δₒ (outbound asymptote) | **+4.385°** | JPL Horizons |
| V∞ | **12.115 km/s** | JPL Horizons |
| ΔV (P₁ term) | **+0.107 mm/s** | Anderson formula |
| \|P₂(cosδ_peri)\| | **0.9991** | Near maximum |

**Prediction:**
```
If only P₁ (pure Anderson):  ΔV ≈ +0.11 mm/s  (below detection)
If P₂ component exists:      |ΔV| ≈ 1–3 mm/s   (dominant)

Decision threshold:
  |ΔV| < 0.5 mm/s  →  supports pure Anderson (P₁ only)
  |ΔV| > 1.0 mm/s  →  supports existence of P₂ component
```

### Europa Clipper Earth Flyby — 2026-12-03

| Parameter | Value | Source |
|-----------|-------|--------|
| δᵢ (inbound asymptote) | **+29.34°** | JPL Horizons (NAIF: −159) |
| δₒ (outbound asymptote) | **+30.61°** | JPL Horizons |
| V∞ | **11.596 km/s** | JPL Horizons |
| ΔV (P₁ term) | **+0.397 mm/s** | Anderson formula |
| \|P₂(cosδ_peri)\| | **0.616** | Above threshold |

**Prediction:**
```
If only P₁ (pure Anderson):  ΔV ≈ +0.40 mm/s  (marginal detection)
If P₂ component exists:      |ΔV| ≈ 1–2 mm/s   (dominant)

Falsification: |ΔV| > 3 mm/s  →  outside all framework parameters
```

**Both flybys have near-zero P₁ terms. Any anomaly > 1 mm/s directly tests the P₂ component.**

---

## Excluded Mechanisms

The following mechanisms have been quantitatively excluded:

- Solar wind truncation of plasmasphere (Lpp always outside B_main)
- 7.3× amplification mechanism (spurious — volume integral gives η = 1)
- Plasma coupling explaining B = 394 km (no matching plasma scale)
- Multipole expansion explaining Juno zero (unphysical coefficients, overfitting)
- Space debris angular momentum (10¹⁶× smaller than Earth)
- Dark energy direct effect (10⁴⁰× wrong scale)

---

## Open Problems

| Problem | Status | Priority |
|---------|--------|----------|
| RQ12: Theoretical origin of κ = 1/B_main | Open | High |
| RQ4: Juno zero result — additional mechanism | Open | High |
| RQ2: Rigorous derivation of two-way Doppler factor 2 | Candidate | Medium |
| RQ13: Physical mechanism of ap correlation | Open | Low |

---

## Repository Structure

| File | Contents |
|------|----------|
| `01_Observations.md` | Flyby data, NASA OMNIWeb ap/F10.7 |
| `02_Constraints.md` | Observational constraints, closed orbit theorem, GPS analysis |
| `03_Hypotheses.md` | LNSS/Perturbation Model, dark matter hypothesis |
| `04_Mathematics.md` | Anderson formula, GEM derivation, volume integral, factor 2 |
| `05_Predictions.md` | Sealed predictions for JUICE 2026 and Europa Clipper 2026 |
| `06_Falsification.md` | Falsification conditions |
| `07_Open_Problems.md` | RQ1–RQ14 open research questions |
| `Appendix_Data.md` | Symbol table, constants, references |

---

## Historical Flyby Data

| Flyby | ΔV (mm/s) | ap | \|P₂(cosδ_peri)\| | Result |
|-------|-----------|-----|-------------------|--------|
| Galileo I (1990) | +3.92 | 8 | 0.165 | Anomaly |
| Galileo II (1992) | −4.60 | 26 | 0.389 | Anomaly |
| NEAR (1998) | +13.46 | 4 | 0.567 | Anomaly |
| Cassini (1999) | −2.00 | 28 | 0.091 | Anomaly |
| Rosetta I (2005) | +1.82 | 2 | 0.347 | Anomaly |
| Messenger (2005) | ≈0 | 1 | 0.036 | Null |
| Juno (2013) | 0.00 | 29 | 0.031 | Null (RQ4) |

Classification by \|P₂\|_c = 0.06: **7/7 correct**

---

*This is independent research. All predictions were sealed before the flyby dates.*  
*Verification dates: JUICE 2026-09-28/29 · Europa Clipper 2026-12-03*
