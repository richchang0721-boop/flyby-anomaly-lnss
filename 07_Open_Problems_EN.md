# 07 — Open Research Questions

**Last updated:** 2026-06-28 v1.4

---

## Priority Summary (2026-06-28)

| RQ | Problem | Priority | Status |
|----|---------|----------|--------|
| RQ1+RQ2+RQ12 | Field equation → factor 2 + B_main | **High** | Route B pending |
| RQ4 | Juno zero result — additional mechanism | **High** | Open |
| RQ13 | Physical mechanism of ap correlation | Medium | Positioned as secondary effect |
| RQ11 | Dark matter + plasma compound medium | Low | Conceptual exploration |
| RQ14 | Theoretical value of \|P₂\|_c | Medium | Framework established |

---

## RQ1: What is the Field Equation? (partial answer, coupled to RQ2 and RQ12)

**2026-06-28 update:**

The factor of 2 (RQ2) and B_main (RQ12) are coupled — or rather, were coupled before the two-way Doppler resolution (see RQ2). The true question is:

> **What field equation naturally produces the correct single-way amplitude (ωR/c) and determines κ from first principles?**

**Route B target (pending):**
Find a field equation such that the volume integral naturally gives ωR/c, and the wavenumber κ is predicted rather than fitted.

GEM angular structure (sinθ) is already confirmed from GR. The remaining work: derive κ = 1/B_main from the background field equation.

**Status:** GR angular structure confirmed; amplitude and κ origin pending Route B | **Priority: High**

---

## RQ2: Factor of 2 in Anderson Formula (resolved candidate, 2026-06-28)

**Answer: Two-way (two-way) Doppler tracking.**

Anderson et al. used two-way Doppler — signal travels Ground → Spacecraft → Ground. Each leg experiences the Lense-Thirring metric perturbation h₀φ once, giving:

```
Single-way Doppler: ΔV = (ωR/c) · (cosδᵢ − cosδₒ)
Two-way Doppler:    ΔV = 2·(ωR/c) · (cosδᵢ − cosδₒ)  ← Anderson formula
```

This decouples RQ2 from RQ12. B_main = 16,076 km is correct (matches single-way amplitude ωR/c); the factor of 2 comes from the measurement method, not the field equation.

**Pending rigorous derivation:** Whether the outbound and return path integrals are strictly equal when the spacecraft moves rapidly.

**Status:** Candidate resolved; rigorous derivation pending | **Priority: Medium**

---

## RQ4: Juno Zero Result — Additional Mechanism Required (2026-06-28)

**Precise formulation:**

Juno's P₁ path integral is large (should give +8.62 mm/s). All multipole path integrals are co-signed positive:

| Mode | I_Pl | Contribution |
|------|------|-------------|
| P₁ | 0.283 | +8.62 mm/s |
| P₂ | 0.186 | +5.66 mm/s |
| P₃ | 0.082 | +2.49 mm/s |
| P₄ | 0.001 | ≈ 0 |

No physical multipole field structure can cancel all positive contributions simultaneously. The P₁+P₂+P₃+P₄ fit gives unphysical coefficients (large magnitudes, alternating signs) — clear overfitting with n=7 and 4 free parameters.

**Status:** Problem precisely formulated; additional mechanism unknown | **Priority: High**

---

## RQ11: Background Field Origin (Dark Matter + Plasma Hypothesis)

**Calculation results (2026-06-28):**

| Candidate | Characteristic length | vs B_main |
|-----------|----------------------|-----------|
| Dark energy (Λ) | ~5,300 Gpc | 10⁴⁰× |
| Local dark matter | ~10⁶ km | ~100× |
| Fuzzy DM (m~10⁻¹⁴ eV) | ~2×10⁷ km | ~1,364× |
| Jeans instability (ρ_bg=6.34 kg/m³) | = B_main | = 1 (self-consistent) |

The "factor of 100" gap between local dark matter's characteristic length and B_main is potentially meaningful — not a random large number. A local dark matter concentration mechanism of ~100× near Earth could close the gap.

**External connection:** If Crespi et al. (2026) fermionic dark matter core model is confirmed, galactic DM distribution needs recalculation, potentially modifying local density estimates.

**Status:** Direct DM/DE effects excluded; compound medium hypothesis open | **Priority: Low**

---

## RQ12: Theoretical Origin of κ = 1/B_main

**Precise formulation (after two-way Doppler resolution of RQ2):**

B_main = 16,076 km matches the single-way amplitude. The question reduces to:

> **What background field equation gives wavenumber k = 6.22×10⁻⁸ m⁻¹?**

Dimensional analysis: k cannot be constructed from Earth's fundamental constants (M_E, J_E, ω_E, R_E). It must be a property of the background field Ψ_bg.

If Yukawa interpretation: m_eff = ℏk/c = 12.3 feV/c² (ultra-light boson, ~10⁹× lighter than axion).

**Route B target:** Derive k from a candidate background field equation; compare to 6.22×10⁻⁸ m⁻¹.

**Status:** Numerically determined; theoretical origin open | **Priority: High**

---

## RQ13: Physical Mechanism of ap Correlation (2026-06-28)

**Three candidate mechanisms tested:**

| Mechanism | Test | Result |
|-----------|------|--------|
| B: Plasmapause truncation | B_eff ∝ Lpp scaling | ✗ Excluded (Lpp always > B_main) |
| A: Coherence disruption | exp(−ap/ap₀) suppression | ✗ Insufficient (Galileo II, Cassini still anomalous at high ap) |
| C: Geometric coincidence | ap vs \|P₂\| correlation | △ r = −0.60 (partial) |

**Conclusion:** ap is a second-order modifier (c₂ = −0.249 mm/s/nT). The r = −0.72 correlation partially reflects the Juno geometric confound. Physical mechanism of the remaining genuine ap effect is open.

**Status:** Positioned as secondary effect; mechanism open | **Priority: Low (n>10 flybys needed)**

---

## RQ14: Theoretical Value of |P₂|_c

**Theoretical estimate:**
```
|P₂|_c = σ_track / (V∞ · K · |A₂| · |I_P2|) ≈ 0.041
```

Observed gap: 0.036 (Messenger, null) to 0.091 (Cassini, anomaly) → midpoint ≈ 0.06

**Key insight:** |P₂(cosδ_peri)| is a **proxy for orbital symmetry**, not a direct field strength measure. δ_peri does not enter the path integral. When perigee lies near ±54.7°, inbound and outbound segments become nearly mirror-symmetric, causing I_P2 → 0.

The A₂/A₁ estimate is unreliable with n=7 (heavily influenced by Juno's large residual). More flyby data required.

**Status:** Theoretical framework established; precise value requires n>10 | **Priority: Medium**
