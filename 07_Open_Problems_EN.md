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

**Core idea (proposed by Mao Lin Chang):**

The existing framework (spherical harmonics, retarded Green's functions) assumes the spacecraft **passively reads** the background field Ψ_bg — the field is unaffected by the spacecraft's presence. Candidate 4 proposes the opposite class of mechanism: the spacecraft, in passing through the medium, **actively perturbs it**, and this perturbation backreacts on the spacecraft's trajectory.

---

### ★ Independent Literature Support (added in 2026-07-01 review): The DSN Tracking Gap

During the 2026-07-01 document review, a literature search revealed a previously unrecorded methodological fact that directly supports Candidate 4:

**The Anderson anomaly's operational definition is not a continuous path integral.** Bertolami et al. (2010, arXiv:1201.0163) state explicitly:

> *"The effect...showed the impossibility of fitting the trajectory with a single hyperbolic arc, but allowed for a separate fit of the inward and outward paths...highly localized at the perigee, where tracking through the Deep Space Network (DSN) is not available (with an approximate four hours gap)."*

In other words, ΔV is actually measured by **separately fitting inbound and outbound hyperbolic arcs and comparing their asymptotic velocities** — the ~4-hour window near perigee is untracked and effectively invisible.

**Implications for the framework:**

The existing Legendre path-integral formula (P₁+P₂+P₃...) implicitly assumes the effect is a "force accumulated continuously along the path." But if the **actual measurement method itself** compares two separately-fit arcs across an invisible gap, then:

1. The path-integral formula may simply be a mathematical convenience that happens to give the correct boundary-term answer, not evidence that the physical mechanism is truly continuous
2. The real physical event is very plausibly **localized near perigee** (within the DSN gap), not distributed along the entire trajectory
3. This is exactly the physical picture Candidate 4 ("medium backreaction") originally assumed — the effect concentrated where the spacecraft is closest and perturbs the medium most strongly

**This is currently the strongest independent support for Candidate 4** — not a guess of ours, but a methodological detail revealed by the original anomaly-measurement literature itself, previously unnoticed by this framework.

**Follow-up direction:** If a localized event near perigee is real, RQ4 (Juno's zero result) may need reframing — from "why doesn't the path integral vanish" to "why did a localized perigee event fail to occur (or get cancelled by some unknown condition) specifically in the Juno case." This is a new angle not yet formalized.

---

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

**Core idea (proposed by Mao Lin Chang):**

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

---

### Rigorizing Candidate 4: Gravitational Self-Force (MiSaTaQuWa Equations) (2026-07-01)

**Background:** While searching for "an established formula from another field that could compute Candidate 4," we found a mature, published theory in General Relativity — gravitational self-force, used for modeling extreme-mass-ratio-inspiral trajectories in LISA gravitational-wave source modeling.

**Mathematical form (MiSaTaQuWa equations):**

```
Du^μ/dτ = -1/2(g^μν+u^μu^ν)(2∇h_tail - ∇h_tail) u^λu^ρ

h_tail(τ) = 4m ∫_{-∞}^{τ-ε} ∇[G_ret(z(τ), z(τ′))] u^μ′u^ν′ dτ′
```

The tail term is an integral over the entire past worldline, determined by the background spacetime's **retarded Green's function** — not an arbitrary power-law kernel, but a memory kernel determined by the physics (the field equation itself).

**Key known property (confirmed in the literature):** Pure gravitational self-force has **no local term** analogous to the electromagnetic ALD force (a term proportional to jerk) — the effect comes entirely from the tail integral; the instantaneous part contributes nothing.

**Mapping to Candidate 4:** If the spacecraft itself couples weakly to the LNSS background field Ψ_bg, its own perturbation, scattered back by the field structure created by Earth's rotation (δΨ_Earth), would produce a tail-type backreaction force — this is not new physics, but an application of an established self-force formalism to our already-established background field framework.

### Quick Test: Jerk on a Real Hyperbolic Trajectory (Ruling Out the Local ALD Hypothesis)

Using a real Keplerian hyperbolic trajectory (not the earlier tanh toy model), we computed peak jerk near perigee to test the ALD-type (local, jerk-proportional) hypothesis:

| Flyby | Peak jerk (m/s³) | dV_obs |
|-------|-------------------|--------|
| Rosetta I | 7.27×10⁻³ | +1.82 |
| Galileo I | 1.39×10⁻² | +3.92 |
| NEAR | 1.54×10⁻² | +13.46 |
| **Juno** | **1.74×10⁻²** | **0.00** |
| Cassini | 1.76×10⁻² | −2.00 |
| Galileo II | 1.89×10⁻² | −4.60 |

**Conclusion: Failed.** Juno's and Cassini's peak jerk are nearly identical (1.74 vs 1.76×10⁻²) — Juno again cannot be separated by a purely local instantaneous quantity, the third such failure (following speed retardation and Cherenkov intensity).

**The positive side of this failure:** It rules out a local ALD-type self-force, and the literature tells us pure gravitational self-force **inherently lacks** this local term — today's negative result is consistent with the known mathematical structure of MiSaTaQuWa theory, not a refutation of it, and indirectly supports the case that the effect must come from a non-local tail integral.

**Honest scope statement:** A full calculation requires (1) deriving the retarded Green's function for our background field equation ∇²δΨ−κ²δΨ=S, (2) numerically integrating the tail term along the full past worldline of the hyperbolic trajectory, (3) computing the gradient of this tail field to get the self-force, (4) integrating the self-force along the trajectory to get the ΔV correction — this is graduate-thesis-level computational work, beyond today's scope. **Status:** Candidate 4 now has a rigorous theoretical foundation for the first time (not an analogy); full calculation pending | **Priority: Medium (theoretical foundation established, computation substantial)**

---

### Candidate 6: Jump Conditions / Scattering Framework (2026-07-01)

**Core question (raised by Mao Lin Chang):** Candidates 4, 5, and the fractional calculus attempts all presuppose that "integration" is a necessary mathematical tool. But why must it be an integral?

**Reflection:** The Anderson formula `ΔV = V∞K∫sinδdδ` is written as an integral, but its value depends only on the boundary (cosδᵢ, cosδₒ), not on the path taken in between — the integral sign itself may be redundant packaging. The only solid reason to use an integral is "the field propagates at finite speed, requiring integration over history" (as in MiSaTaQuWa's retardation).

**Two findings from today, taken together, point to a neglected option:**
1. Jerk (a local, instantaneous quantity) fails to separate Juno for the third time
2. The DSN tracking gap: we have never observed what happens inside perigee passage — only "before" and "after"

**This suggests:** Perhaps the right question is neither "what does the path integral accumulate" nor "what happens at this instant," but rather what **algebraic relationship** connects the "before" and "after" states — what happens in between need not be known at all.

**Two established, integral-free physics languages:**

| Framework | Core idea | Fit to the problem |
|-----------|-----------|---------------------|
| Scattering theory (S-matrix) | `|out⟩ = S|in⟩` — relates only incoming/outgoing states, all detail packaged into S | Directly matches the fact that DSN cannot see inside perigee |
| Israel junction conditions (GR jump conditions) | Algebraic jump conditions matching two spacetime regions (the GR analog of shock jump conditions), no integration over the interface needed | Closer to our already-established GR framework than fluid shocks |

**Verification: this framework naturally reproduces the Anderson formula**

Defining a potential Φ(δ) = −K·cosδ, the simplest jump condition is:

```
ΔV/V∞ = Φ(δₒ) − Φ(δᵢ) = K(cosδᵢ − cosδₒ)
```

**This is exactly the Anderson formula.** In form, Anderson's formula was already a jump condition, not the product of a path integral — the path integral was merely an optional, redundant intermediate step.

**A new angle on Juno:** Perhaps the P₂/P₃ corrections should not be "additional terms added to a path integral," but rather a richer structure in the jump condition's potential function Φ(δ) itself (possibly non-analytic, possibly threshold-like) — this may be the same underlying idea as Candidate 5 (nonlinear coupling) and the lower-rated "Topology" entry in GPT's language table, worth re-evaluating.

**Status:** Concept proposed and verified to reproduce the Anderson formula (P₁ term); the specific form of P₂/P₃ corrections under this framework not yet formalized or computationally tested | **Priority: Medium (novel concept, directly echoes DSN gap evidence, but requires formalization)**

---

### Candidate 7: Topological Classification (2026-07-01)

**Background:** GPT's language evaluation table originally rated Topology lowest (★★☆☆☆), but Candidate 6's discovery that both the closed-orbit theorem and the Anderson formula are fundamentally topological arguments motivated a serious re-examination.

**Core idea:** P₂(cosδ) has nodal lines at δ=±54.7356° (exact value, not fitted), dividing declination space into three regions:

```
North cap N: δ > 54.7356°
Equatorial band B: −54.7356° < δ < 54.7356°
South cap S: δ < −54.7356°
```

**Classification rule (parameter-free):** If any of the trajectory's three characteristic angles (δᵢ, δ_peri, δₒ) has an absolute value exceeding the exact node 54.7356°, classify as "leaves the equatorial band" → predict anomaly. If all three fall within the band, classify as "never leaves" → predict null result.

**Verification against historical data:**

| Flyby | δᵢ | δ_peri | δₒ | Region sequence | Ever leaves band? | dV_obs | Classification |
|-------|-----|--------|-----|-----------------|---------------------|--------|-----------------|
| Galileo I | −12.5° | −61.8° | 34.3° | B-S-B | Yes | +3.92 | Anomaly ✓ |
| Galileo II | −34.3° | 74.2° | −4.5° | B-N-B | Yes | −4.60 | Anomaly ✓ |
| NEAR | −20.8° | −32.5° | 72.0° | B-B-N | Yes | +13.46 | Anomaly ✓ |
| Cassini | −12.9° | 58.5° | −5.0° | B-N-B | Yes | −2.00 | Anomaly ✓ |
| Rosetta I | −2.8° | −71.4° | 34.3° | B-S-B | Yes | +1.82 | Anomaly ✓ |
| Messenger | 31.4° | 53.3° | −31.9° | B-B-B | No | +0.02 | Null ✓ |
| Juno | −2.0° | 53.5° | −48.9° | B-B-B | No | 0.00 | Null ✓ |

**Classification accuracy: 7/7 = 100%, with zero fitted parameters** (the node location 54.7356° is P₂'s exact theoretical zero).

**This rule explains something the |P₂(cosδ_peri)| threshold (RQ14) cannot:** NEAR's enormous anomaly (+13.46 mm/s) — its perigee δ_peri=−32.5° lies within the equatorial band, but its **outbound direction** δₒ=+72.03° far exceeds the node. A perigee-only |P₂| criterion misses this; a topological rule examining all three characteristic points of the trajectory correctly classifies it.

**★★★ Critical divergence from the |P₂(cosδ_peri)| threshold: the JUICE 2026 sealed prediction ★★★**

Both criteria perform "equally perfectly" on the n=7 historical dataset, but they give **opposite** conclusions for the already-sealed JUICE 2026-09-28/29 prediction:

| Criterion | Value | JUICE prediction |
|-----------|-------|-------------------|
| \|P₂(cosδ_peri)\| (RQ14, already sealed) | 0.9991 (δ_peri≈1.4° near equator, large P₂ value) | If P₂ term exists, anomaly should be observable |
| **Topological criterion (Candidate 7, new)** | **max(\|δᵢ\|,\|δ_peri\|,\|δₒ\|)=4.385° (far below node 54.7°)** | **Null result, same class as Juno/Messenger** |

This is a textbook symptom of an underdetermined model with n=7 — two logically distinct criteria both fit historical data perfectly, yet diverge out-of-sample. **JUICE 2026-09 will be the first opportunity to discriminate between these two criteria**; see 05_Predictions_EN.md for the specific sealed prediction.

**Status:** 7/7 historical classification success with zero free parameters; gives an opposing prediction to the existing RQ14 criterion for JUICE, now recorded as an independent sealed prediction; the physical mechanism (why the node itself, rather than the continuous P₂ value, determines classification) not yet formalized | **Priority: High (clear, imminent discriminating test)**

---

## Current Highest Priority (2026-07-01, sole valid version, supersedes all previous versions in this document)

**Important new findings (added during this review):**

**The DSN tracking gap — direct literature support for Candidate 4.** The Anderson anomaly's operational definition is not a continuous path integral, but rather "impossible to fit the trajectory with a single hyperbolic arc, requiring separate inbound/outbound fits" — the effect is highly localized near perigee, which is precisely where DSN tracking is unavailable for roughly 4 hours (Bertolami et al. 2010, arXiv:1201.0163). This suggests the existing P₁/P₂/P₃ path-integral formulas may simply be "a mathematical trick that happens to give the right boundary-term answer," while the true physical mechanism is more likely a localized event near perigee — directly supporting Candidate 4 (medium backreaction) over a continuous-field-reading model.

**Missing OSIRIS-REx (2017-09-22) data point.** Perigee altitude 17,237 km, just outside B_main = 16,076 km, with ~34% field retention predicted and an observed anomaly upper limit of <0.1 mm/s. This is a natural boundary test case for B_main and should be included in 01_Observations_EN.md as an eighth data point.

**Gravitational self-force (MiSaTaQuWa) — Candidate 4's first rigorous theoretical foundation.** A jerk calculation on a real hyperbolic trajectory ruled out local ALD-type self-force, indirectly supporting pure gravitational self-force (no local term, effect entirely from tail memory integral). Full calculation requires the retarded Green's function — graduate-thesis-level work.

**Candidate 6: jump conditions / scattering framework — questioning whether integration is necessary.** The Anderson formula itself can be reinterpreted as a jump condition ΔV/V∞=Φ(δₒ)−Φ(δᵢ), requiring no path integral. This framework naturally echoes the DSN gap evidence (only "before" and "after" are known, never "during") and offers a fresh angle on P₂/P₃ corrections and Juno's zero result.

**Candidate 7: topological classification — gives an opposite prediction to RQ14 for JUICE 2026.** Using P₂'s exact node (54.7356°) to divide declination into three regions, and testing whether any of the trajectory's three characteristic angles ever leaves the equatorial band, achieves 7/7 on historical data with zero free parameters. But it gives a prediction for JUICE 2026-09 directly opposite to the existing |P₂(cosδ_peri)| criterion (RQ14) — a textbook symptom of an underdetermined n=7 model, which the JUICE observation will directly adjudicate.

**Priority list:**

1. **[Highest priority, new] The JUICE 2026-09-28/29 observation will adjudicate the diverging predictions of Candidate 7 vs. RQ14** — this is currently the framework's strongest discriminating test
2. **[New] Formalize Candidate 6's jump-condition framework**, attempt to re-express P₂/P₃ corrections within it, and test whether it gives a more physically reasonable Juno cancellation condition than the path-integral approach
3. **[New] Formalize why Candidate 7 classifies by "the node itself" rather than "the continuous P₂ value"** — currently an empirical finding lacking a first-principles derivation
4. **[New] Formally integrate the DSN tracking gap's methodological significance into Candidate 4**, and assess whether it reframes RQ4
5. **[New] Add OSIRIS-REx to the formal dataset** (01_Observations_EN.md) as an independent test of the B_main boundary
6. **[New, long-term] Derive the retarded Green's function for the LNSS background field equation**, compute the full gravitational self-force tail integral (graduate-thesis-level work, not a near-term goal)
7. **Rigorous derivation of the two-way Doppler factor of 2** (RQ2) — confirm outbound and return path integrals are strictly equal
8. **Derive the theoretical origin of κ = 1/B_main** (RQ12) — the sole remaining unknown of the background field Ψ_bg
9. **Await Europa Clipper (2026-12-03) observational results** — sealed prediction already recorded

**Removed/superseded content:**
- Three earlier priority lists (dated 2026-06-26, 2026-06-27, 2026-06-28) have been marked outdated and removed, as some of their conclusions (e.g., the B_main=19,828km candidate value) have been overturned by the two-way Doppler analysis
- "Search for JUICE 2024 official analysis" is no longer necessary — the 2024 flyby altitude was too high (6,840 km), the framework already predicted no significant effect, and this research direction has been superseded by precise 2026 data
- The "whole-path weighting" direction for the fractional memory kernel (see the two toy model attempts under the Candidate 4 upgrade above) has been ruled out as an entire model class; Candidate 6 offers a structurally different alternative, to be prioritized over further fractional-calculus variants
