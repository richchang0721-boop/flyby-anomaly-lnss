# 04 — Mathematics

**Last updated:** 2026-06-28 v1.4

---

## The Anderson Formula

```
ΔV = V∞ · (2ωR/c) · (cosδᵢ − cosδₒ)
K = 2ωR/c = 3.097 × 10⁻⁶
```

Where:
- V∞ = hyperbolic excess velocity (km/s)
- ω = Earth rotation rate = 7.292 × 10⁻⁵ rad/s
- R = Earth mean radius = 6,371 km
- δᵢ = inbound asymptote declination
- δₒ = outbound asymptote declination

---

## Boundary Term Interpretation

The Anderson formula arises naturally as a **boundary term** of the path integral:

```
ΔV = V∞ · K · ∫sinδ dδ = V∞ · K · [−cosδ]_{δᵢ}^{δₒ}
   = V∞ · K · (cosδᵢ − cosδₒ)
```

The integrand sinδ corresponds to the Legendre P₁ mode. Higher-order terms (P₂, P₃, ...) contribute corrections.

---

## GR Derivation: Why sinθ Appears Naturally

In the weak-field GEM (Gravitomagnetic ElectroMagnetic) framework, a rotating mass generates a gravitational vector potential:

```
A_φ(r, θ) = −(2GJ/c²r²) · sinθ · φ̂
```

The sinθ angular structure emerges directly from General Relativity — this is not an assumption of the LNSS framework.

**The gravitomagnetic field:**
```
B_g = ∇ × A_g
B_r = 2A₀(r) cosθ / r
B_θ = −sinθ (A₀/r + A₀')
```

---

## Factor of 2: Two-Way Doppler Tracking (2026-06-28)

### Key insight

Anderson et al. used **two-way Doppler tracking**: a signal travels Ground → Spacecraft → Ground. The Lense-Thirring metric perturbation h₀φ is experienced **twice** — once on the outbound leg and once on the return leg:

```
Single-way Doppler: ΔV = (ωR/c) · (cosδᵢ − cosδₒ)
Two-way Doppler:    ΔV = 2·(ωR/c) · (cosδᵢ − cosδₒ)  ← Anderson formula
```

The factor of 2 is a property of the **measurement method**, not the field equation. The GEM field equation naturally gives ωR/c (single-way); the two-way tracking doubles it.

**Pending rigorous derivation:** Whether the outbound and return path integrals are strictly equal when the spacecraft moves rapidly during the flyby.

---

## Closed Orbit Theorem (2026-06-28)

**Theorem:** The Anderson effect is exactly zero for any closed orbit.

**Proof:**
```
ΔV = V∞ · K · (cosδᵢ − cosδₒ)
Closed orbit: start = end → δᵢ = δₒ
Therefore: ΔV = V∞ · K · (cosδᵢ − cosδᵢ) = 0  □
```

**ISS verification (inclination 51.6°):**
```
Ascending to +51.6°:   ∫sinδ dδ = +0.3789
Descending to equator: ∫sinδ dδ = −0.3789
Descending to −51.6°:  ∫sinδ dδ = +0.3789  [cos(−51.6°) = cos(+51.6°)]
Ascending to equator:  ∫sinδ dδ = −0.3789
Total:                              = 0.000000 (exact)
```

**This is a topological necessity**, not an approximation. ISS, GPS, Starlink, space debris — all closed orbits are exactly immune to the Anderson effect.

### Two Kinds of Zero Result

| Zero result | Mechanism | Type |
|-------------|-----------|------|
| LEO/GPS/Starlink/ISS | δᵢ = δₒ, topological cancellation | **Topological necessity, ΔV ≡ 0** |
| Juno (open flyby) | Perigee near P₂ node (53.5° ≈ ±54.7°) | Geometric coincidence, ΔV ≈ 0 |
| Messenger (open flyby) | δᵢ ≈ −δₒ, nearly symmetric orbit | Geometric coincidence, ΔV ≈ 0 |

---

## Two Decay Length Scales (key insight, 2026-06-28)

The critical correction: Busack's B = 394 km is **not** the decay length of the main LNSS field.

| Field component | Decay length | Physical meaning | Equation type |
|----------------|-------------|-----------------|---------------|
| δΨ_P₁ (main field, Anderson) | B_main >> flyby altitude (~thousands of km) | Why Anderson formula has no altitude dependence | Modified Helmholtz, κ_main very small |
| δΨ_CMB (secondary, Busack) | B_Busack = 394 km | Decay of CMB anisotropy term | Modified Helmholtz, κ = 1/394 km |

**Why Anderson has no altitude correction term:**

If B_main >> 2,000 km (maximum flyby altitude), then:
```
exp(−h/B_main) ≈ 1  for all flyby altitudes h ∈ [300, 2000] km
```

The field is essentially constant across all historical flyby heights — this is a natural consequence, not an assumption.

---

## Perturbation Model: Boundary Value Problem (2026-06-27)

**Decomposition:** Total field Ψ = Ψ_bg (background) + δΨ (local perturbation)

**Background field equation (free space, no source):**
```
∇²Ψ_bg + k²Ψ_bg = 0
```

**Perturbation field equation (Modified Helmholtz / Yukawa type):**
```
∇²δΨ − κ²δΨ = S(M, J, r, θ)
δΨ(r→∞) = 0
l=1 solution: δA_φ(r,θ) = C₁ · K₁(κr)/r · sinθ
```

where K₁ is the modified Bessel function (exponentially decaying solution).

---

## Volume Integral and B_main Determination

**η = 1: No amplification mechanism needed (2026-06-27)**

The volume integral:
```
C₁ = (4G/c²) · ∫₀^{R_E} ρ · ω · r³ · K₁(κr)/(κr) dV
```

When B_main = 16,076 km, this integral gives exactly the Anderson coefficient. The previous "7.3× amplification problem" was a spurious issue caused by using only the surface boundary condition rather than the full volume integral.

**Numerical solution:**
```
B_main = 16,076 km = 2.52 R_E
κ_main = 1/B_main = 6.22 × 10⁻⁸ m⁻¹
```

**Field strength at flyby altitudes (B_main = 16,076 km):**

| Flyby | Altitude (km) | Field retained |
|-------|--------------|----------------|
| Galileo II | 303 | 98.1% |
| NEAR | 539 | 96.7% |
| Juno | 561 | 96.6% |
| Galileo I | 960 | 94.2% |
| Cassini | 1,172 | 93.0% |
| Rosetta I | 1,954 | 88.6% |
| Messenger | 2,347 | 86.4% |

---

## B_main and Plasmasphere Validation (2026-06-28)

B_main = 16,076 km (L = 3.52) falls within the plasmasphere range during active conditions (Lpp ≈ 3.3–5 R_E).

**Carpenter & Anderson (1992) formula:**
```
Lpp = 5.7 − 0.47 × Kp_max
```

All historical flybys had Lpp > B_main_L = 3.52. **Solar wind truncation of the plasmasphere is excluded** as a mechanism.

**Honest assessment:** B_main's correspondence with the plasmasphere range is noted, but B_main does not correspond to any specific known plasmasphere boundary. It is the characteristic length of the background field Ψ_bg, whose physical origin remains an open problem (RQ12).

---

## Factor 2 and B_main: Decoupled (2026-06-28)

An earlier analysis suggested that the factor of 2 and B_main might be coupled (matching ωR/c vs 2ωR/c gives different B_main values). This was resolved by identifying the factor of 2 as coming from two-way Doppler tracking:

- Factor of 2 source: two-way Doppler (measurement method)
- B_main = 16,076 km: matches ωR/c (single-way field amplitude)

The two problems are **decoupled**. B_main = 16,076 km is the correct value.

---

## ap Correlation: Mechanism Testing (RQ13, 2026-06-28)

### Signal hierarchy (established 2026-06-28)

**Primary (dominant):** Geometry — P₂ node at ±54.7°, r = 0.852, zero free parameters

**Secondary (modifier):** ap index — c₂ = −0.249 mm/s/nT, second-order effect

**Tertiary:** Moon-Sun tidal geometry — 26% RMS improvement

### ap Mechanism Tests

| Mechanism | Test | Result |
|-----------|------|--------|
| B: Plasmapause truncation | B_eff ∝ Lpp scaling | ✗ Excluded (Lpp always > B_main) |
| A: Geomagnetic coherence disruption | exp(−ap/ap₀) suppression | ✗ Insufficient (Galileo II, Cassini still anomalous at high ap) |
| C: Geometric coincidence | ap vs \|P₂\| correlation | △ Partial (r = −0.60, n=6) |

**Conclusion:** ap is a second-order modifier, not the primary driver. Juno's zero result is primarily geometric (P₂ node). The ap correlation r = −0.72 is partly a confound effect from Juno having both high ap and low |P₂|.

**Best-fit linear model:**
```
ΔV = 3.80 + 0.579·ΔV_Anderson − 0.249·ap
RMS = 2.11 mm/s (51% improvement over Anderson alone)
```

---

## Juno Cancellation Analysis (2026-06-28)

**Path integrals for Juno (δᵢ = −2°, δₒ = −48.9°):**

| Mode | I_Pl | Contribution (mm/s) |
|------|------|---------------------|
| P₁ | 0.283 | +8.62 |
| P₂ | 0.186 | +5.66 |
| P₃ | 0.082 | +2.49 |
| P₄ | 0.001 | ≈ 0 (geometric cancellation) |

**Multipole fit results:**

| Model | RMS | Juno prediction | Physical? |
|-------|-----|----------------|-----------|
| P₁ only | 3.82 mm/s | +8.62 | ✓ Physical |
| P₁+P₂ | 2.75 mm/s | +4.91 | △ A₂ = −1.98 (marginal) |
| P₁+P₂+P₃ | 0.61 mm/s | +0.37 | ✗ A₁=11.8, A₂=−25.4 (unphysical) |
| P₁+P₂+P₃+P₄ | 0.14 mm/s | 0.000 | ✗ Overfitting (n=7, 4 parameters) |

**Conclusion:** All path integral modes for Juno are co-signed positive. No physical multipole field structure can cancel them. **Juno's zero result requires a mechanism outside the current framework.** (RQ4)

---

## |P₂|_c Theoretical Analysis (RQ14, 2026-06-28)

**Theoretical threshold:**
```
|P₂|_c = σ_track / (V∞ · K · |A₂| · |I_P2_typical|)
         ≈ 0.041
```

Observed gap: 0.036 (Messenger, null) to 0.091 (Cassini, anomaly) → midpoint ≈ 0.06

**Key insight:** δ_peri does not directly enter the path integral. The Anderson formula and P₂ path integral depend only on δᵢ and δₒ. The |P₂(cosδ_peri)| correlation (r = 0.852) reflects **orbital symmetry** — when perigee falls near ±54.7°, the inbound and outbound segments become nearly mirror-symmetric, causing the P₂ path integral to vanish.

---

## Complete Derivation Chain

```
Step 1: GR weak-field expansion (harmonic gauge)
   h₀φ ∝ (2GJ/c²r²) sinθ
   → sinθ angular structure emerges from GR ✓

Step 2: Volume integral determines amplitude
   C₁ = (4G/c²)∫ρωr³K₁(κr)/(κr)dV
   → At B_main = 16,076 km: A = ωR/c ✓

Step 3: Two-way Doppler tracking (factor of 2)
   Outbound + return legs each experience h₀φ once
   → Signal frequency shift doubled ✓

Step 4: Anderson formula
   ΔV = 2·(ωR/c)·(cosδᵢ − cosδₒ) ✓

Sole remaining unknown: κ = 1/B_main (origin of background field wavenumber)
```

---

## Background Field Properties (from B_main)

If κ = 1/B_main arises from an unknown medium, the medium must satisfy:

```
Equivalent density:  ρ_bg = ω_E²/(4πG) = 6.34 kg/m³
Field wave speed:    v_p = ω_E × B_main = 1,172 m/s
Jeans length:        λ_J = v_p/√(4πGρ_bg) = B_main  (self-consistent)
```

Local dark matter density (3×10⁻²² kg/m³) gives a characteristic length ~10⁶ km — approximately 100× larger than B_main. This factor of 100 is a potentially meaningful signal, not a random large number. (See 03_Hypotheses_EN.md, Hypothesis RQ11)
