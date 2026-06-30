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

### RQ4 Methodological Extension (2026-06-30): Is the Problem Limited by the Mathematical Language Itself?

**Inspiration:** Observing that Chen Lijie et al. (UCSD, 2026) broke a decade-old bottleneck in the SETH lower bound proof for the "furthest pair" problem — not by finding a cleverer integer technique, but by re-expressing the problem in algebraic number fields instead of integers. The breakthrough came from changing the mathematical language, not from a smarter proof within the existing one.

**Application to RQ4:**

The current language — Legendre multipole expansion (P₁, P₂, P₃, P₄...) — implicitly assumes the field is an **instantaneous, memoryless function of angle**. The path integral depends only on the instantaneous inbound/outbound geometry.

**A specific hypothesis tested and rejected:**

> Hypothesis: Juno's high velocity (V∞) causes significant retardation effects that invalidate the spherical harmonic expansion.

**Test:** Cassini's V∞ = 16.0 km/s is far higher than Juno's 9.82 km/s, yet Cassini shows a significant anomaly (−2.0 mm/s) rather than a null result. If retardation were speed-dominated, Cassini should be more affected than Juno — the opposite of what is observed.

**Conclusion: This specific hypothesis is directly refuted by the data and is excluded.**

**The deeper methodological question remains open:**

Ruling out "speed → retardation" does not rule out the broader concern that spherical harmonic expansion itself may be the wrong language. Open question:

> Does a **path-dependent** (rather than purely angle-dependent) field description exist, under which Juno's multipole coefficients become physically reasonable (rather than the current large-magnitude, alternating-sign values)?

---

### Candidate 4: Medium Backreaction (detailed, 2026-06-30)

**Core idea (proposed by Rich Chang):**

The existing framework (spherical harmonics, retarded Green's functions) assumes the spacecraft **passively reads** the background field Ψ_bg — the field is unaffected by the spacecraft's presence. Candidate 4 proposes the opposite class of mechanism: the spacecraft, in passing through the medium, **actively perturbs it**, and this perturbation backreacts on the spacecraft's trajectory.

**Distinction from simple friction:**

Pure friction F ∝ −v (always opposing velocity, purely dissipative) has already been excluded by the data — it can only explain deceleration, not the mixed-sign ΔV seen in the Anderson effect (NEAR: +13.46, Galileo II: −4.60). Candidate 4 is not friction, but draws on fluid dynamics concepts:

| Mechanism | Physical picture | Directionality |
|-----------|------------------|-----------------|
| Added mass effect | Accelerating body must "drag" surrounding medium, increasing effective inertia | Changes effective inertia, not simple deceleration |
| Wake-induced backreaction | Body leaves a wake; if medium is elastic, wake may push or pull the body | Can be positive or negative |
| Cherenkov-like effect | If spacecraft speed exceeds medium wave speed v_p, shock radiation carries away momentum | Directional (cone angle) |

**Preliminary test: the simple "intensity ∝ speed" version is excluded**

Background field wave speed v_p = ω_E × B_main ≈ 1.172 km/s. Mach numbers M = V∞/v_p for all flybys:

| Flyby | M | sin²θ_Cherenkov | Cherenkov cone angle θ_C |
|-------|---|------------------|---------------------------|
| Rosetta I | 3.30 | 0.908 | 72.3° |
| Messenger | 3.46 | 0.917 | 73.2° |
| NEAR | 5.85 | 0.971 | 80.2° |
| Galileo II | 7.57 | 0.983 | 82.4° |
| Galileo I | 7.64 | 0.983 | 82.5° |
| **Juno** | **8.38** | **0.986** | **83.2°** |
| Cassini | 13.66 | 0.995 | 85.8° |

Juno (M=8.4) and Cassini (M=13.7) have nearly identical Cherenkov intensity factors (< 1% difference), yet opposite outcomes. **The simple "speed determines backreaction intensity" version is excluded**, suffering the same fate as the retardation hypothesis.

**What remains viable: directionality, not intensity**

True Cherenkov radiation is not a monotonic function of speed but is concentrated within a specific cone angle θ_C = arccos(1/M), with strong directionality. If this radiation cone couples with the spacecraft trajectory geometry (e.g., the angle relative to the perigee tangent direction) through resonance or cancellation, this — not the cone angle value itself — may be what determines Juno's outcome.

**Status:** Simple intensity version excluded; directional/geometric coupling version untested, requires fluid-structure coupling mathematics beyond the current Helmholtz path-integral framework | **Priority: Low (conceptual record, requires new mathematical tools)**

---

### Candidate 4 Upgrade: Fractional Calculus as the Language of Memory Effects (2026-06-30, GPT suggestion)

**Background:** GPT proposed an evaluation table of seven candidate mathematical languages for describing "path," "memory," and "long-range coupling" — structures that Candidates 4 and 5 require but the current Legendre spherical harmonic expansion cannot provide.

| Mathematical Language | Describes | Relation to Existing Candidates |
|-----------------------|-----------|----------------------------------|
| Legendre Harmonics | Angle (current approach) | Known limitation (Juno same-sign problem) |
| Functional (path functional) | Whole path | Formal mathematical skeleton for Candidate 5 |
| Delay Equation | Fixed delay | Concrete form of Candidate 4's "retarded Green's function," but must avoid a single delay scale |
| **Fractional Calculus** | **Memory (power-law decay)** | **Key upgrade for Candidate 4, see below** |
| Non-local Field | Long-range coupling | Spatial version of Candidate 5 |
| Dynamical System | Resonance | Corresponds to Candidate 4's "directional/geometric coupling" version |
| Topology | Path classification | Same origin as the established closed-orbit theorem, but limited use for Juno's fine structure |

**Why fractional calculus may resolve what has stalled Candidate 4:**

The previously tested "speed retardation" (Candidate 4 initial version) and "Cherenkov intensity" hypotheses both died on the same counterexample — Cassini (V∞=16.0 km/s) is faster than Juno (V∞=9.8 km/s), yet Cassini shows a more significant effect. Both share a common flaw: **each assumes a single characteristic time/speed scale**, and is therefore inevitably refuted by a simple "which is faster" ordering.

Fractional calculus memory effects (d^α Ψ/dt^α, 0<α<1) are not a fixed delay but a **continuous spectrum of power-law decay** — every moment in history contributes, decaying as a power law rather than exponentially or as a step function, with **no single "characteristic speed" available for simply ranking different flybys**. This structurally avoids the counterexample form that defeated the earlier hypotheses.

**Status:** Concept proposed, not yet formalized or computationally tested. Next step, if pursued: build a toy model with a fractional memory kernel and test whether it can simultaneously fit Juno (null) and Cassini (anomaly) without introducing a single characteristic scale | **Priority: Low (conceptual record; requires specialized fractional calculus tools beyond the current framework)**

---

### First Toy Model Test (2026-06-30): Unsuccessful, but Instructive

**Model design:**

```
ΔV_frac = ∫ (d cosδ/dt) × K_frac(t_now − t) dt
K_frac(τ) = τ^(α-1) / Γ(α)    [Caputo fractional memory kernel]
```

Spacecraft trajectory modeled as a smooth tanh transition from δᵢ to δₒ, with transition sharpness proportional to each flyby's V∞.

**Test results:**

| α | Cassini/Cassini(α=1) | Juno/Juno(α=1) |
|---|----------------------|----------------|
| 1.00 | 1.0000 | 1.0000 |
| 0.70 | 0.3410 | 0.3452 |
| 0.30 | 0.0499 | 0.0514 |
| 0.10 | 0.0091 | 0.0095 |

**Conclusion: Failed.** The two decay curves nearly overlap — the fractional memory effect suppresses Cassini and Juno proportionally, producing no selective differentiation (cannot drive Juno toward zero while preserving Cassini's anomaly).

**Root cause diagnosis:** The model scaled transition sharpness with spacecraft speed V∞, but the fractional kernel is insensitive to the transition's *shape* — only to the *temporal distribution* of the transition. When both flybys' time axes are scaled by their own speeds, the kernel sees similar relative historical structure for both, producing no differentiation.

**Directions suggested by this failure (untested):**

1. **τ should be a characteristic time scale of the field itself, not the spacecraft.** Different flybys should share the same memory kernel (scaled by field propagation speed v_p, not spacecraft speed V∞), rather than each being independently rescaled — this echoes the insight retained after the "speed retardation" hypothesis failed in Candidate 4.

2. **Memory effects should act on a specific field component (e.g., P₂), not a blanket weighting of the entire path.**

3. **α itself may couple to the perigee value |P₂(cosδ_peri)|**, rather than being an independent free parameter — this would connect Candidate 4 to the already-established P₂ calm-zone evidence (RQ14), rather than introducing a new mechanism from scratch.

**Status: First model tested and failed; failure mode points to three specific correction directions, pending further verification | Priority: Low (requires more precise physical assumptions to proceed)**

---

### Second Toy Model Test (2026-06-30): Field-Native Time Scale, Still Unsuccessful

**Correction applied (following direction 1 from the first failure's diagnosis):**

Instead of scaling the memory kernel's time axis by spacecraft speed V∞, use the field's own characteristic time scale:

```
τ_field = B_main / v_p = 16,076 km / 1,172 m/s ≈ 13,713 s ≈ 3.81 hours
t_transit = 2·B_main / V∞   (physical time for spacecraft to cross the full field range)
ratio = t_transit / τ_field
```

Ratios for each flyby fall between 0.15–0.61 — a meaningful competitive range (unlike the first version, where all ratios clustered near 0.005 with no differentiation).

**Test results (fixed α=0.5, comparing fractional correction to standard P₁ value):**

| Flyby | t_transit (s) | frac/P1 ratio |
|-------|---------------|----------------|
| Cassini | 2,008 | −0.563 |
| **Juno** | **3,274** | **−0.640** |
| NEAR | 4,693 | −0.689 |
| Galileo I | 3,593 | −0.715 |
| Galileo II | 3,622 | −0.545 |

**Conclusion: Failed.** Juno's ratio (−0.640) falls within the middle of the range for other significantly anomalous flybys (−0.545 to −0.715), showing no anomaly or distinctiveness.

**Broader negative result:**

Two consecutive attempts (v1: spacecraft time scale; v2: field time scale) failed at the same point — **a fractional memory kernel applied to the "entire path" tends to scale all flybys' effects proportionally, rather than selectively suppressing a specific flyby (Juno)**. This rules out not just a parameter choice, but the entire class of models combining "fractional memory + blanket path weighting."

**Direction for a more precise follow-up:**

What is needed is not parameter tuning but a change in what is being weighted — shifting the fractional memory weight from "the entire path" to "only the P₂-mode path integral" (echoing direction 2 from the first failure's diagnosis). This is a structurally different model requiring redesign:

```
Concept: ΔV = ΔV_P1 (standard, instantaneous) + A₂ × ∫ [P₂ path integrand] × K_frac(τ; α) dt
```

Keeping P₁ instantaneous (already well-established) and applying memory correction only to the P₂ component — this way the correction acts only on the secondary, yet-to-be-explained part, without diluting the verified P₁ physics.

**Status: Both whole-path-weighted model versions tested and failed (negative result, ruling out an entire model class); next step requires a structurally different model (P₂-only weighting), not implemented today | Priority: Low**

---

### Candidate 5: Nonlinear Field Coupling (detailed, 2026-06-30)

**Core idea (proposed by Rich Chang):**

A complete physical picture in four layers: (1) background field Ψ_bg as a uniform "sea"; (2) Earth's rotation perturbs this sea, forming local field structure δΨ_Earth; (3) the spacecraft flies through this **already-perturbed** field; (4) the Earth-Moon-Sun three-body system further shapes the field.

The existing framework handles layers (1)(2)(4) (Perturbation Model + three-body framework), but implicitly assumes for layer (3) that the spacecraft is a **passive reader** — measuring only the field's pre-existing value along its trajectory — and that all perturbation sources (Earth rotation, lunar-solar tides, solar wind) **linearly superpose** without coupling:

```
Current implicit assumption:
  δΨ_total = δΨ_Earth + δΨ_Moon-Sun + δΨ_solar-wind  (independent)

Candidate 5 proposes:
  The spacecraft's local perturbation effect may couple nonlinearly with
  "the shape the background field has already been molded into by other
  sources," rather than simply adding.
```

**Explanatory power: rationalizing the ap effect**

If pure linear superposition holds, ap (solar-wind-induced field perturbation) and the spacecraft's Anderson path-integral effect should be independent — the path integral depends only on trajectory geometry (δᵢ, δₒ), and ap should have no reason to alter it.

But the data clearly show a real second-order ap correction (c₂ = −0.249 mm/s/nT, see 02_Constraints_EN.md). **If nonlinear coupling exists** — where the spacecraft's local perturbation effect depends on "the shape the background field has currently been molded into by solar wind" — then the ap effect has an intuitively reasonable physical mechanism, rather than being merely an empirically fitted coefficient.

**Relationship to Candidate 4:**

Candidate 4 asks "does the spacecraft perturb the field?" (passive vs. active reading); Candidate 5 asks "do multiple perturbation sources couple?" (linear superposition vs. nonlinear interaction). These may be facets of the same deeper mechanism — if the spacecraft does actively perturb the field (Candidate 4), that perturbation would naturally couple with the background field's current state (Candidate 5) rather than superposing independently.

**Status:** Concept proposed, not yet formalized or computationally verified; requires nonlinear field equations beyond the current linear Helmholtz framework | **Priority: Low (conceptual record; may share a deeper mechanism with Candidate 4)**

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
