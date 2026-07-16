# 07 — Open Research Questions

**Last updated:** 2026-07-14 v2.1 (RQ12 Route B second attempt: Mexican-hat potential confirmed as parameter matching, v/λ unidentifiable)

---

## Priority Summary (2026-07-02)

| RQ | Problem | Priority | Status |
|----|---------|----------|--------|
| **All 7 flybys reconstruction** | δᵢ, δₒ, δ_peri recomputed via Horizons for all historical flybys | **Highest** | **Complete** — see dedicated section below |
| **Candidate 7** | Topological node classification | — | **Overturned** — δ_peri contributed 0/7 correct classifications |
| RQ4 | Juno zero result | High | P1 prediction corrected to ~6.0–6.3 mm/s (was 10.4); still unresolved |
| RQ1+RQ2 | Field equation angular structure + factor 2 | Low | **Resolved** |
| RQ12 | B_main / κ origin | Low | Cannot be derived from Earth-local physics; reframed as free parameter |
| RQ13, RQ15 | ap correlation; geomagnetic drift | — | **Premises relying on old Cassini δ_peri now known false; pending re-evaluation** |
| RQ11 | Dark matter + plasma compound medium | Low | Conceptual exploration |
| RQ14 | Theoretical value of \|P₂\|_c | Medium | Framework established, but underlying δ_peri now suspect |

---

## 2026-07-02 Session Summary

**RQ1+RQ2 closed.** Angular structure (sinθ) remains derived from GR/GEM. RQ2's remaining rigor gap closed: the outbound/return leg asymmetry from spacecraft motion during round-trip light time is O((v_sc/c)²) ≈ 1.6×10⁻⁹ relative — two orders of magnitude below the Anderson signal itself (~10⁻⁷), unobservable at DSN precision. The two-way Doppler factor-of-2 mechanism is now closed with a quantified error bound.

**RQ12 (κ origin): Route B executed, no derivation found — problem reframed.** Extended dimensional analysis (5 new Earth-local combinations tested: geosynchronous radius, c/ω_E, geometric mean, Kerr-type length — all fail) confirms κ is not built from Earth-local constants. Reframed into two falsifiable sub-hypotheses: (i) Ψ_bg is an intrinsic background-field constant (effective mass 1.228×10⁻¹⁴ eV/c²), independent of local space environment; (ii) κ is set by a local medium (e.g. plasmasphere) and should track ap/F10.7.

**Discriminating test (single-flyby κ_i inversion, n=5):** κ_i vs F10.7 shows r=−0.044 (clean null). The marginal κ_i vs ap signal (r=−0.69, p=0.075) is diagnosed as a Cassini-driven leverage artifact via leave-one-out (Cassini's geometric term is smallest of the five, and its residual 0.93 mm/s sits within Anderson-formula precision itself). The four geometrically healthy flybys show κ_i spread of only ~5% while their ap spans 2–26. **Conclusion: existing data supports hypothesis (i).** RQ12 status: cannot be derived from Earth-local physics; reclassified as a framework free parameter, theoretical origin deferred to field theory/cosmology.

**RQ4: Gated Anderson model (candidates 6+7 combined), zero free parameters.**
```
ΔV = V∞·(2ωR/c)·(cosδᵢ−cosδₒ) × Θ(max(|δᵢ|,|δ_peri|,|δₒ|) > 54.7356°)
```
RMS(P₁-only) = 3.953 mm/s → RMS(gated) = 0.381 mm/s (90% improvement); Juno residual goes from −10.41 to 0. Tested against literature angles for Rosetta III: gate=0, gated model hits observation (0±0.1 mm/s) exactly, while pure P₁ predicts +1.091 mm/s — an **11σ falsification of the un-gated Anderson formula** using already-published data.

**🔴 Urgent: data integrity audit.** Cross-checking against Jouannic et al. 2015 (ISSFD) and Acedo 2017 (arXiv:1701.05735):
1. **δ_peri definition conflict.** Galileo I's orbital inclination (142.9°, Acedo) bounds the equatorial-frame perigee declination to ≤37.1°. The repository's δ_peri = −61.8° exceeds this physical bound — it cannot be the equatorial position declination as currently labeled. The gated model's 7/7 result rests entirely on this column; using literature perigee latitudes instead causes the gate to fail on Galileo I/II, Cassini, and Rosetta I (all of which have observed anomalies but literature latitudes place them inside the equatorial band).
2. **Juno asymptotic angles are an outlier vs. two independent literature sources** (both give δᵢ≈−14.3°, δₒ≈+39.4°, vs. repository's δᵢ=−2.0°, δₒ=−48.9°). RQ4's conclusion is unaffected either way, but the repository value needs verification.
3. **Cassini's observed value is disputed in the literature** (−2 mm/s per Anderson 2008 vs. −0.5±0.5 mm/s per later compilations) — this may explain why Cassini repeatedly surfaces as an outlier in independent analyses (κ_i inversion, gated residuals).
4. **Most urgent: sealed predictions' coordinate frame is unverified.** The repository records JUICE/Europa Clipper trajectories as sourced from Horizons in **Ecliptic J2000**, but the Anderson formula's δ requires **equatorial declination**. If the sealed predictions were computed in the wrong frame, both sealed values may need to be recomputed — JUICE flies by 2026-09-28, under three months away.

**Action item (top priority):** Re-derive δᵢ, δ_peri, δₒ for all flybys (including JUICE/Europa Clipper) from JPL Horizons in the equatorial frame, outputting both position declination and velocity-vector declination to settle the δ_peri definition question, before treating the gated model's 7/7 or the sealed predictions as final.

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

**2026-07-02 update — closed:** The asymmetry from spacecraft displacement during round-trip light time is O((v_sc/c)²) ≈ 1.6×10⁻⁹ relative (V∞~12 km/s, r~1.5 R_E), two orders below the Anderson signal (~10⁻⁷), unobservable at DSN precision.

**Status:** Resolved, with quantified error bound | **Priority: Low (complete)**

---

## RQ4: Juno Zero Result — Additional Mechanism Required (2026-06-28, 🔴 input angles corrected 2026-07-02, A₂=0 finding added 2026-07-03)

**🔴 Note:** The table below uses Juno's OLD (now known incorrect) angles (δᵢ=−2°, δₒ=−48.9°). Reconstruction via JPL Horizons found the correct values (δᵢ=+14.16°, δₒ=+39.40°), matching independent literature (Jouannic et al. 2015; Acedo 2017) almost exactly. The corrected P₁-only prediction is **+5.99 to +6.34 mm/s** (not +8.62/+10.4 mm/s as below) — see results.json and the 2026-07-02 update. The table's P₂/P₃/P₄ rows are retained for traceability only; a refit with corrected angles is pending.

**Precise formulation (historical, pending refit):**

Juno's P₁ path integral is large (should give +8.62 mm/s). All multipole path integrals are co-signed positive:

| Mode | I_Pl | Contribution |
|------|------|-------------|
| P₁ | 0.283 | +8.62 mm/s |
| P₂ | 0.186 | +5.66 mm/s |
| P₃ | 0.082 | +2.49 mm/s |
| P₄ | 0.001 | ≈ 0 |

No physical multipole field structure can cancel all positive contributions simultaneously. The P₁+P₂+P₃+P₄ fit gives unphysical coefficients (large magnitudes, alternating signs) — clear overfitting with n=7 and 4 free parameters.

**🆕 2026-07-03: this whole cancellation approach is now directly contradicted by theory.** The GEM-derived requirement for exact Juno cancellation would need A₂/A₁≈−3.4 (see RQ14 addition below), but the GEM field equation's multipole selection rule gives A₂=0 exactly. A₂ cannot be simultaneously 0 and −3.4 — **internal P₁/P₂ cancellation within the GEM framework is now excluded as an explanation for Juno's null result.**

**Status:** Problem precisely formulated; internal GEM cancellation path excluded; additional mechanism still unknown | **Priority: High**

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

### 🆕 RQ12 Route B attempt: are k and κ two branches of the same dispersion relation? (2026-07-14)

**Background:** While discussing with GPT whether Schrödinger/eigenvalue language could derive B_main, a structural check surfaced: the two existing field equations — background ∇²Ψ_bg+k²Ψ_bg=0 (positive sign, oscillatory solutions) and perturbation ∇²δΨ−κ²δΨ=S (negative sign, decaying K₁(κr) solutions) — are currently treated as sharing the same numerical value (k=κ=1/B_main), but have opposite signs, representing oscillatory vs. evanescent regimes. No document has ever given a common equation connecting the two.

**Proposed unifying hypothesis:** If Ψ_bg satisfies a massive Klein-Gordon equation (∂²_t−c²∇²+(m_eff·c²/ℏ)²)Ψ=0, the static (ω=0, source-driven) limit naturally gives k²=−(m_eff·c/ℏ)², i.e. k becomes purely imaginary, k=iκ with κ=m_eff·c/ℏ — this is the standard derivation of the Yukawa screening solution, exactly matching δΨ's equation.

**Connection to an existing result:** κ=m_eff·c/ℏ is the same formula already used earlier in RQ12 to compute m_eff=ℏκ/c=1.228×10⁻¹⁴ eV/c² (originally just a Yukawa-mass side note) — this isn't a new proposal; it connects two previously-computed but unconnected results.

**Derived falsifiable prediction:** If this unification holds, the background field Ψ_bg can no longer be "uniform and static" — it must genuinely oscillate in time at frequency ω≈m_eff·c²/ℏ (a truly static massive KG field at ω=0 only yields decaying solutions, never the oscillatory ones the background equation requires). This ω implies a specific period, testable against known dynamical timescales in the system.

**Calculation and test result:**

```
ω = m_eff·c²/ℏ = 18.66 rad/s
Period T = 2π/ω = 0.3368 s

Comparison:
  vs. Earth's rotation period (86,164 s): shorter by 255,831×
  vs. solar wind dynamic pressure variability (~1,800–36,000 s): shorter by 5,344–106,888×
  vs. Juno's Doppler integration timescale (1,000 s, per Iorio 2019): shorter by 2,969×
```

**Conclusion: the T=0.34 s oscillation frequency matches no known physical dynamical timescale in the framework, off by at least three orders of magnitude in every comparison. The specific "background field oscillates at the m_eff-implied frequency" version of the unification hypothesis is excluded.**

**Honest note on a process error:** In the first pass, Claude's comparison logic was wrong and incorrectly judged T to fall within the solar wind timescale range; this was caught on review and corrected — recorded here per the project's standing "errors are not hidden" principle.

**Scoping, to avoid overclaiming:** This test only excludes the most direct literal version ("m_eff as a literal oscillation frequency"). The broader question of whether k and κ share some other unifying structure remains open — this specific attempt failed, not the general idea.

**Status:** One concrete RQ12 Route B attempt completed and failed (a negative result with clear elimination power, not a vague abandonment); the broader k/κ unification possibility remains open; the origin of κ as the background field's intrinsic characteristic length is still unresolved | **Priority: Medium (narrows the search space, but the main question remains open)**

---

### 🆕 RQ12 Route B, another attempt: a Mexican-hat potential can fit m_eff, but v/λ/α are unidentifiable (2026-07-14)

**Background:** Discussion with GPT explored writing Ψ_bg as an ultra-light scalar background field φ_bg, coupled to Earth's GEM vector field A_μ via a Higgs-portal-like mechanism, written as `[□+m_eff²(φ_bg)]A_μ=α(φ_bg)J_μ`. GPT proactively supplied a concrete potential to test this:

```
V(φ) = λ(φ²−v²)²/4    (Mexican-hat potential, standard symmetry-breaking form)
Take v=1 eV, λ=7.533×10⁻²⁹
→ ⟨φ⟩=v, m_eff=√V''(v)=1.227×10⁻¹⁴ eV
```

**Verification result: the math checks out.** Step-by-step verification with SymPy: V'(v)=0 (confirms v is genuinely a minimum, not an arbitrary substitution); V''(v)=2λv² (standard mass-squared definition); solving gives λ=7.5399×10⁻²⁹, a 0.09% relative difference from GPT's 7.533×10⁻²⁹ (rounding in intermediate steps, not an arithmetic error).

**But GPT itself honestly flagged this as "parameter matching, not a first-principles derivation," and noted "α is not determined by V(φ); it requires an independent interaction term," and "the current framework does not yet provide a symmetry, boundary eigenvalue, or independent physical scale that uniquely fixes v, λ, and α" — these judgments were checked and confirmed correct, and quantified to show the severity:**

```
V(φ)=λ(φ²−v²)²/4 has two free parameters (v,λ) but only one number (m_eff)
to fit — one equation, two unknowns, with infinitely many solutions:

  v=1×10⁻³ eV → λ=7.540×10⁻²³  (still gives m_eff=1.228×10⁻¹⁴ eV)
  v=1×10⁰  eV → λ=7.540×10⁻²⁹  (still gives m_eff=1.228×10⁻¹⁴ eV)
  v=1×10³  eV → λ=7.540×10⁻³⁵  (still gives m_eff=1.228×10⁻¹⁴ eV)
  v=1×10¹⁰ eV → λ=7.540×10⁻⁴⁹  (still gives m_eff=1.228×10⁻¹⁴ eV)
```

**v spans 13 orders of magnitude, with λ automatically compensating to always reproduce the same m_eff — a textbook case of parameter unidentifiability. Every (v,λ) pair is "mathematically correct," but none of them is a prediction — all are post-hoc fits.**

**A methodological point worth recording on its own:** GPT's three self-assessments (parameter matching not derivation; α undetermined; no independent constraint exists) matched exactly what Claude confirmed and quantified after checking — a concrete instance of cross-model discussion operating per the project's established "Perspective Generator, not Truth Validator" principle. GPT did not declare victory upon producing a number that "looked right"; it proactively flagged its own limitations — this restraint is itself more worth recording than the proposal's content.

**Conclusion: this path (φ_bg + Higgs-portal-style coupling) is currently not viable, in the same status as χ_boundary — the language is usable and mathematically self-consistent, but lacks a derivation path independent of the already-known answers (m_eff, B_main). Until v, λ, and α are given an independent physical origin, this framework cannot be used to explain any residual.**

**Status:** Math verified but confirmed to be parameter matching, not derivation; v/λ unidentifiability quantitatively demonstrated; classified alongside χ_boundary and the Patrick tensor-field proposal as "unresolved degrees of freedom" | **Priority: Low (conceptual recording value only, not a usable tool, pending independent constraints before re-evaluation)**

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

### 🆕 RQ14/RQ4 key addition: A₂ = 0 in the GEM framework — P₂ requires a mechanism outside pure Earth rotation (2026-07-03)

**Background:** Both RQ14 and RQ4 were stuck on "what should A₂ be" — different flybys gave mutually contradictory A₂/A₁ estimates (from −0.005 to −3.4), suggesting A₂ isn't a stable free parameter at all. This section derives A₂'s theoretical value directly from the GEM field equation's multipole structure, rather than continuing to fit it from data.

**Derivation (GEM current-multipole selection rule):** Earth's rotational mass current J(r') = ρ(r')(Ω×r') = ρ(r')Ω r' sinθ' φ̂' has an angular dependence that is exactly sinθ'φ̂' — a pure l=1 pattern. In the multipole expansion of the vector potential, angular and radial integrals separate; the current's angular shape alone determines which l survive. **As long as Earth's density is spherically stratified (ρ=ρ(r'), not required to be uniform) and rotation is rigid, the vector potential's multipole expansion has l=1 only — l=2 vanishes exactly, regardless of the interior density profile's shape.**

**Confirmed directly in the literature (not just by analogy):** Iorio (2019, MNRAS) cites the exact formula from Panhans & Soffel (2014, *Classical and Quantum Gravity*):

```
φ_gm = -(GS/r²) Σᵢ [(-1)ⁱ/((2i+3)(2i+5))] (R_eε/r)^(2i) P_(2i+1)(ξ)
     = -(GS/r²) [2ξ - (6/7)(R_eε/r)²P₃(ξ) + ...]
```

The expansion contains only P₁, P₃, P₅... (odd orders) — l=2 is structurally absent, not merely small. Earth's real l=3 term (spin-octupole) arises from the coupling between rotation (l=1) and oblateness J₂ (l=2 shape), matching the formula's ∝G·S·J₂/c² dependence exactly.

**Implications for the framework:**
1. If A₂ (the P₂ amplitude) were meant to arise from "the same GEM mechanism, next order," its theoretical value should be zero. The mutually inconsistent A₂/A₁ values fitted across flybys now have an explanation: **A₂ shouldn't exist in the first place — any nonzero fitted value is likely noise or another effect masquerading as an l=2 gravitomagnetic signal.**
2. If a genuine P₂ effect exists, it cannot come from Earth's rotation via a simple next-order GEM correction — it would require a mechanism outside the framework (e.g., an intrinsic l=2 structure in the background field Ψ_bg itself, RQ12), not "the natural extension of P₁."
3. **RQ4's Juno-cancellation condition (requiring A₂≈−3.4) is now directly contradicted** — theory gives A₂=0, which cannot simultaneously equal −3.4. This further supports that Juno's null result needs a mechanism outside GEM's P₁/P₂ path-integral framework, not an internal cancellation.

**Byproduct: P₃ (l=3) magnitude estimate — the first theoretical backing for the previously "very low confidence" P₃ hypothesis.** Using Earth's flattening (f=1/298.257), the A₃/A₁ amplitude ratio is estimated at roughly 1/300 to 1/2000 depending on flyby altitude. If P₁ effects are mm/s-scale, P₃ is estimated at **0.01–0.05 mm/s** — well below current DSN tracking precision (~0.1 mm/s), consistent with 05_Predictions_EN.md's prior (previously unsupported) "very low confidence, needs a dedicated mission" assessment.

**Honest confidence levels:**
- A₂=0 (no l=2 current multipole): **high confidence**, directly confirmed by a cited literature formula, independent of Earth's interior density profile details
- P₃ magnitude estimate (0.01–0.05 mm/s): **medium confidence**, an amplitude-ratio order-of-magnitude analogy, not a rigorous re-derivation of the boundary-term integral; a sealed-prediction-quality number would require converting Iorio's orbital-precession formalism into a single-pass boundary-term ΔV formula (as was done for P₁ in 04_Mathematics_EN.md) — not yet done

**Status:** A₂=0 established; P₂ requires a mechanism outside simple Earth rotation; P₃ gains its first theoretical magnitude estimate | **Priority: Medium-high (clarifies a key confound in RQ14/RQ4, does not directly resolve RQ4 itself)**

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

**Status:** Concept proposed and verified to reproduce the Anderson formula (P₁ term); now formalized as partial-wave scattering language (see 2026-07-03 update below), with P₂/P₃'s specific form given by GEM constraints, and a new round of testing against Juno completed | **Priority: High (formalized, and yields a decisive negative result that shrinks the search space)**

---

### 🆕 Candidate 6 formalized: partial-wave scattering language, GEM-allowed channels excluded as an explanation for Juno (2026-07-03)

**Formalization:** Generalize the already-verified jump condition Φ₁(δ)=−K·cosδ so that each Legendre order l corresponds to an independent scattering channel:

```
Φ_l(δ) = -A_l·P_l(cosδ)
ΔV_l/V∞ = A_l[P_l(cosδᵢ) - P_l(cosδₒ)]
Total: ΔV/V∞ = Σ_l A_l[P_l(cosδᵢ) - P_l(cosδₒ)]
```

In scattering-matrix language: S_l=1 (identity) ↔ channel closed (A_l=0); S_l≠1 ↔ channel open. **This is not new free parameters repackaged — it directly inherits the hard constraints from the GEM derivation above (see the RQ14 addition), not fitted values:**

```
l=1: A₁=K (open, Anderson main term, verified)
l=2: A₂=0 (closed, confirmed by the GEM derivation, not fitted)
l=3: A₃ given by Iorio (2019)'s formula (open but suppressed, not freely fitted; magnitude in 05_Predictions_EN.md's P₃ section)
l=4: expected closed by parity selection rule (even-order current multipoles don't exist)
```

**Key test: can the physically-constrained channels (only odd l=1,3 open) explain Juno?**

Using Juno's corrected angles (δᵢ=+14.16°, δₒ=+39.40°):

```
l=1 channel contribution (A₁=K, theoretical): +5.988 mm/s (the amount that needs cancelling)
l=3 channel contribution (A₃/A₁ in Iorio's range 0.0005–0.0033): +0.013 to +0.084 mm/s
Gap: l=3 is 120–1200× too small, and same sign (adds, doesn't cancel)
```

**Conclusion: if scattering channels are restricted to GEM-allowed odd orders (l=1,3,5...), Juno's null result cannot be explained by internal cancellation within the framework.** This is the fourth test of "can Juno be separated by a single local/geometric quantity" to fail (following speed retardation, Cherenkov intensity, and real hyperbolic-trajectory jerk) — but this one carries more weight, because it fails under a framework with **no free parameters, strictly constrained by theory** (the earlier three failed in a relatively open parameter space; this one fails because theory itself forbids the needed magnitude).

**Implication for the candidate list:** Any future attempt to "add a term that zeroes out Juno" must now contend with this constraint — A₂ and A₄ must be zero, and A₃'s amplitude is fixed by Iorio's formula, not freely adjustable. This shrinks the search space — genuine progress by elimination, not a standstill.

**Status:** Candidate 6 formalized as a partial-wave scattering framework; GEM-allowed channels confirmed unable to explain Juno (a negative result that narrows the search space); Juno still requires a mechanism outside the framework (scattering off the background field Ψ_bg itself, Candidate 4's retarded tail term, or another as-yet-unidentified channel) | **Priority: High**

---

### 🆕 Unifying Candidate 4 and Candidate 6: Non-Local Effective Action (2026-07-14)

**Not a new candidate — a higher-level repackaging of two existing ones; this needs saying up front.**

Discussion with GPT revealed that Candidate 4's (medium backreaction / MiSaTaQuWa) retarded tail term `a_μ(τ)=∫K_μν(τ,τ')u^ν(τ')dτ'` and Candidate 6's (jump conditions / scattering framework) path holonomy `B_hol=logP exp(∫_γ A)` are, structurally, the same mathematical object written two ways — Candidate 6's already-verified jump condition (depending only on boundary angles δᵢ, δₒ, not on the intermediate path) is the special "path-independent" case of this more general holonomy integral. Unified form:

```
S_eff = S_GR + S_LNSS
S_LNSS = ∫d⁴x√(-g) R·F(□)R    (non-local kernel F(□), encodes Candidate 4's memory effect)
B_main = B_local + B_hol + B_tail
  B_local: local rotation/orbital term (known, given by GEM)
  B_hol: holonomy accumulated along the path (Candidate 6's verified boundary jump is its special case)
  B_tail: non-local history term (Candidate 4's retarded effect)
```

**Value of this unification:** not new physics, but the observation that two candidates already independently verified may not be independent hypotheses at all, but different facets of one underlying framework — Candidate 6's success on the P₁ term (exactly reproducing the Anderson formula) and Candidate 4's success explaining the DSN tracking-gap evidence may be the same thing showing up under different observational conditions.

**🔴 A problem that must be flagged: χ_boundary is currently an unresolved degree of freedom, violating the already-established selection-rule principle**

To keep any LNSS correction confined to flybys — not also showing up in GPS/LAGEOS/Gravity Probe B and other long-duration Earth-orbiting satellites' high-precision orbits (a real, serious physical constraint — past attempts at an "enhanced gravitomagnetic field" explanation failed precisely on this consistency issue) — the discussion introduced a boundary-activation function:

```
ΔΓ ∝ χ_boundary · H(γ) · f(Ω⊕, v∞, δ)
```

**χ_boundary currently has no specified form — it is a placeholder.** This runs directly into the principle just established via the partial-wave scattering formalization (see the Candidate 6 section above): any new degree of freedom needs a selection rule or theoretical origin, not a dial that gets turned on or off whenever convenient — the same risk category as the excluded "free P₁+P₂+P₃+P₄ fit (A₂=−25.4, unphysical)." This isn't new physics; it's an adjustable knob added to the model.

**Until χ_boundary is given a concrete form (e.g., derived from GEM selection rules or Candidate 5's dynamic boundary-coupling mechanism) or explicitly excluded, this entire non-local action framework cannot be used to explain any residual — it remains at the level of unified mathematical language only.**

**Suggested path forward (proposed by GPT, judged reasonable and adopted by Claude):**
1. Layer 1: classical effective geometry `Γ̃=Γ+ΔΓ_LNSS`, test whether it fits all flyby data (especially Juno's residual) — but the χ_boundary problem must be resolved before this can actually be executed
2. Layer 2: fiber/holonomy model, relating the effect to parallel transport along the entire path (Candidate 6's verified boundary jump is a special case of this layer)
3. Layer 3: quantum-gravity origin — **only after the first two layers give stable predictions**; introducing this too early would make the model's burden of proof unmanageable

Layer 3 (deeper quantum-gravity/fiber-structure origin) is not prioritized until the χ_boundary problem is resolved — deferred.

**Status:** The Candidate 4+6 mathematical unification is recorded; χ_boundary flagged as an unresolved degree of freedom that blocks this framework from being used for any substantive explanation; the GPB/LAGEOS consistency check has been added to 06_Falsification_EN.md | **Priority: Medium (the unified view has recording value, but the framework cannot be used to explain residuals until χ_boundary is resolved)**

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

### 🔴🔴 Complete Reconstruction of All 7 Historical Flybys: Candidate 7's Node Criterion Overturned (2026-07-02)

**Background:** After the audit found δ_peri's definition undocumented and inconsistent with orbital-inclination physics, all 7 historical flybys were fully reconstructed via JPL Horizons: equatorial frame (ICRF), 1-minute-step precise perigee search, both position and velocity declination computed.

**Perigee altitude validation (all cases):** reconstructed altitudes matched official values to within 25 km (mostly <10 km) across all 7 cases, confirming the method (frame setup, precise perigee search) is reliable.

**Complete results for all 7 cases:**

| Flyby | δᵢ (old→new) | δₒ (old→new) | δ_peri (old→new, pos/vel) | Gate (new) | Observed | Correct? |
|-------|---------------|----------------|------------------------------|------------|----------|----------|
| Galileo I | −12.52→**−12.5** (match) | +34.26→**−34.0** (same magnitude, flipped sign) | −61.8→**+23.81/−25.58** (wrong) | 0 | +3.92 | ✗ Fail |
| Galileo II | −34.26→**−34.25** (match) | −4.50→**−4.90** (close) | +74.2→**−32.45/−21.55** (wrong) | 0 | −4.60 | ✗ Fail |
| NEAR | −20.76→**−20.58** (close) | +72.03→**−72.00** (same magnitude, flipped sign) | −32.5→**+32.84/−51.33** (wrong) | **1** (δₒ alone crosses node) | +13.46 | ✓ Pass |
| Cassini | −12.92→**−12.92** (exact match) | −4.99→**−5.48** (close) | +58.5→**−22.73/−9.32** (wrong) | 0 | −2.00* | ✗ Fail |
| Rosetta I | −2.81→**−2.0** (lower confidence) | +34.29→**−34.04** (same magnitude, flipped sign) | −71.4→**+20.83/−27.13** (wrong) | 0 | +1.82 | ✗ Fail |
| Messenger | +31.44→**+32.2** (close) | −31.92→**−32.91** (close) | +53.3→**+46.92/−0.04** (wrong) | 0 | ≈0.02 | ✓ Pass |
| Juno | −2.00→**+14.16** (completely different) | −48.90→**+39.40** (completely different) | +53.5→**−32.22/+28.57** (wrong) | 0 | 0.00 | ✓ Pass |

*Cassini's observed value is disputed in the literature (−2.00 vs −0.5±0.5 mm/s); see earlier audit notes.

**Core conclusion: δ_peri contributes zero correct classifications across all 7 cases.**

The three correctly classified cases (NEAR, Messenger, Juno) are all decided by δᵢ and δₒ alone — NEAR by δₒ alone crossing the node; Messenger and Juno by both δᵢ and δₒ staying well within the band. δ_peri's value or definition never changes any of these three outcomes. The four misclassified cases (Galileo I/II, Cassini, Rosetta I) all relied on the old database's now-confirmed-erroneous, artificially large δ_peri value to "manufacture" a node crossing; with corrected δᵢ, δₒ (neither of which crosses the node), the classification fails.

**Candidate 7's topological node criterion (dependent on whether δ_peri crosses 54.7356°) does not survive systematic verification.** A simplified criterion using only δᵢ and δₒ (dropping δ_peri entirely) scores identically (3/7), since δ_peri never contributed a single correct classification — this means δ_peri is not merely mis-defined, it should not be part of the criterion at all.

**Major additional finding: Juno's δᵢ, δₒ themselves (not just δ_peri) were wrong.** The new reconstructed values (δᵢ=+14.16°, δₒ=+39.40°) are completely different from the old database (δᵢ=−2.00°, δₒ=−48.90°, different in sign as well as magnitude), but closely match independent literature (Jouannic et al. 2015: δᵢ=+14.17°, δₒ=+39.50°; Acedo 2017: δᵢ=−14.308°, δₒ=+39.409°). **This means RQ4's Juno analysis needs to be entirely recomputed with the new angles:**

```
New Anderson P1 prediction (new angles): +5.99 ~ +6.34 mm/s (depending on V∞ used)
Independently computed by Acedo (2017): 6.3355 mm/s (near-perfect cross-validation)
Old framework claim: +10.4 mm/s (now confirmed to be an artifact of erroneous angles)
```

The magnitude of Juno's "uncancelled anomaly" that RQ4 needs to explain is only about **60% of what was previously claimed** (~6 mm/s, not 10.4 mm/s). RQ4 itself remains unresolved (nonzero prediction vs. zero observation), but the coefficients computed in the "RQ4 Precision" subsection (A₂/A₁≈−3.4, and the P₁+P₂+P₃+P₄ multipole table) were all computed with the wrong angles and are not currently trustworthy. Also, the previously celebrated claim that "Juno's δ_peri=53.5° sits only 1.24° from the node — a razor's-edge coincidence" is false: the new data shows Juno is 15.34° from the node, not a special/marginal case at all.

**Downstream analyses directly affected, requiring re-evaluation:**

| Item | Original claim | Current status |
|------|-----------------|-----------------|
| Candidate 7 topological criterion 7/7 | Established | **Overturned** — δ_peri contributed zero correct classifications |
| Gated Anderson model, 90% RMS improvement | Established | **Needs recomputation** (built on the same δ_peri) |
| RQ13 "Juno vs. Cassini: strongest single constraint" (relies on Cassini δ_peri=58.5°) | Established | **Premise now known false**, needs re-evaluation |
| RQ15 geomagnetic drift extension (relies on Cassini δ_peri=58.5°, "3.76° from node") | Concept confirmed | **Premise now known false**, needs re-evaluation of whether it's still meaningful |
| "Signal hierarchy: geometry (P₂ node, r=0.852) is the dominant factor" | Framework core conclusion | **Built on contaminated \|P₂(cosδ_peri)\|; needs recomputation with all 7 corrected δ_peri values** |
| RQ4 Juno precision (A₂/A₁≈−3.4 etc.) | Established | **Computed with wrong angles; needs recomputation** |
| Anderson P1 formula, δᵢ/δₒ reliability | — | **Validated well in 6/7 cases** (Juno excepted, whose δᵢ/δₒ must be fully replaced with new values) |

**Status:** All 7 cases fully reconstructed; Candidate 7's topological criterion systematically overturned; δ_peri should be removed from the criterion; RQ4's Juno analysis needs recomputation with new angles; multiple downstream analyses (signal hierarchy, RQ13, RQ15) built on the same contaminated δ_peri are now marked as unresolved pending recomputation | **Priority: Highest**

---

### RQ15: Secular Geomagnetic Drift as a Slow Boundary-Condition Modulator (2026-07-01, proposed by GPT, verified and corrected)



**Background:** GPT raised the question of whether long-term drift of the magnetic north pole affects the LNSS framework's coupling geometry. The original estimate extrapolated from the 2025-2026 instantaneous drift rate (36 km/year) back to historical cumulative drift — this extrapolation is flawed, since pole drift accelerated substantially after the 1990s (from roughly 15 km/yr up to 50-60 km/yr by the 2010s) and cannot be linearly back-extrapolated.

**Corrected magnitude check (2026-07-01):**

Using historical geomagnetic pole positions, the magnetic north pole drifted a cumulative **9.3°** in geographic angular distance from Galileo I (1990) to Juno (2013) — larger than GPT's original estimate, and **of the same order of magnitude as the P₂ calm-zone width (~5°, 52.3°–57.2°)**.

**Physical assessment (agreeing with GPT's direction, but raising its priority):**

```
If the LNSS source term is purely Earth's rotating mass flow (geographic axis):
  The Anderson main term 2ωR/c is unaffected by magnetic pole drift (geographic
  rotation axis unchanged)

If the LNSS background field couples to the magnetosphere/plasma structure:
  Pole drift changes the coupling boundary's geometric orientation
  → affects the "effective node location," ap coupling efficiency, SAA weak-field
    zone position
  → this is a second-order/boundary-condition effect, not a rewrite of the main model
```

**Testable hypothesis:** For a historical flyby whose δ_peri lies close to the calm-zone edge (e.g., Cassini's 58.5°, only 3.76° from the node), does recalculating the "effective node" position relative to the historical magnetic axis (via IGRF/WMM historical models) reduce the residual compared to using the geographic node?

**Status:** Magnitude verification complete (9.3° cumulative drift, same order as calm-zone width, not negligible); specific IGRF-corrected recalculation for each flyby not yet performed | **Priority: Medium (clear testable method, but a slow second-order effect)**

---

### Candidate 5 Update: Nonlinear Dynamic Boundary Coupling (2026-07-01, proposed by GPT, confirmed)

**Background:** GPT pointed out that solar wind's influence on the LNSS field should not be modeled as "a fixed-shape field multiplied by a suppression coefficient," but rather as "solar wind dynamically reshaping the field boundary's geometry." This is not a new mechanism — it is the concrete physical realization of Candidate 5 (nonlinear field coupling) — merged into Candidate 5 rather than creating a new Candidate 8.

**Core revision:**

```
Original implicit assumption (tested in RQ13):
  δΨ_total = δΨ_Earth + f(ap)   (ap as a linear suppression coefficient)

Candidate 5 updated version:
  δΨ_total(t) = F[δΨ_Earth, Boundary_solarwind(t)]
  (solar wind does not add a term — it dynamically changes the boundary
  condition of the solution itself)
```

**Why this explains ap's known partial effectiveness (RQ13's known limitation):**

ap is a scalar proxy for geomagnetic disturbance intensity, losing directional information. The physical quantities actually determining boundary deformation may be:

```
Solar wind dynamic pressure
IMF Bz direction (north-south component determines magnetopause reconnection efficiency)
Magnetopause standoff distance
Plasmasphere L-shell (already computed via the Carpenter-Anderson formula in 02_Constraints_EN.md)
Magnetic Local Time (MLT) at perigee
```

**Relationship to Candidate 6:** If the field is instantaneously deformed by solar wind near perigee, the Anderson anomaly would more closely resemble a "before entering the deformed boundary" → "crossing" → "after leaving the deformed boundary" structure, which aligns closely with Candidate 6 (jump conditions / scattering framework) — not a slowly-accumulating path integral, but an instantaneous boundary jump.

**Actionable next step:** Obtain IMF Bz and solar wind dynamic pressure data for the historical flyby dates from NASA OMNIWeb (ap and F10.7 already obtained, see 01_Observations_EN.md), and test whether these finer-grained parameters explain the "observed value minus pure P₁ prediction" residual better than ap alone.

**Status:** Concept revised and confirmed (proposed by GPT, verified in agreement by this framework); specific parameters not yet obtained, not computationally tested | **Priority: Medium (clear actionable next step, data obtainable from NASA OMNIWeb)**

---

## Current Highest Priority (2026-07-02, sole valid version, supersedes all previous versions in this document)

**🔴🔴🔴 All 7 historical flybys have now been fully reconstructed via JPL Horizons. Candidate 7's topological criterion is systematically overturned; δ_peri should be removed from the framework.**

Full results and the complete 7-flyby table are in the "Complete Reconstruction of All 7 Historical Flybys" section above. Core conclusion: δ_peri contributed zero correct classifications across all 7 cases; the 3 cases Candidate 7 got right (NEAR/Messenger/Juno) are all decided by δᵢ, δₒ alone, independent of δ_peri. Juno's δᵢ, δₒ themselves were also found to be wrong; the reconstructed values match independent literature (Jouannic 2015, Acedo 2017) almost exactly. RQ4's Juno P1 prediction should be corrected from +10.4 mm/s to ~6.0–6.3 mm/s.

**Priority list (updated):**

1. **[Highest priority] Formally update all 7 flybys' δᵢ, δₒ, δ_peri in 01_Observations_EN.md** (superseding old values) — **done, see 01_Observations_EN.md v1.6**
2. **[Highest priority] Downgrade Candidate 7 to "overturned"; recompute the Gated Anderson model's 90% RMS improvement with the new angles** (likely to drop substantially, since much of the original improvement came from "fixing" Juno, and Juno's δᵢ, δₒ have now also changed)
3. **[High] Fully recompute RQ4's Juno analysis**: recalculate the P1/P2/P3/P4 path integrals and the A₂/A₁ coefficient using the new angles (δᵢ=+14.16°, δₒ=+39.40°)
4. **[High] Recompute the |P₂(cosδ_peri)| correlation (originally r=0.852) using the new δ_peri for all 7 cases; determine whether the framework's core "geometry is the dominant factor" claim still holds**
5. **[High] Re-evaluate or remove RQ13 and RQ15 sections that rely on Cassini's δ_peri=58.5°**
6. **[High] JUICE 2026-09-28/29 observation** — sealed prediction's coordinate frame confirmed correct; but since Candidate 7 itself is now overturned, the comparison framing at reveal time needs adjustment
7. Resolve Cassini's observed-value discrepancy (−2 vs −0.5±0.5 mm/s)
8. Formally add Rosetta II/III and EPOXI I–III (six data points) to 01_Observations_EN.md (sources: Jouannic 2015, Acedo 2017)
9. Obtain IMF Bz and solar wind dynamic pressure data for historical flybys (NASA OMNIWeb), test whether they explain the residual better than ap (Candidate 5 extension)
10. Formalize Candidate 6's jump-condition framework (does not depend on δ_peri, unaffected by this session's findings)
11. Formally integrate the DSN tracking gap's methodological significance into Candidate 4
12. Derive the retarded Green's function for the LNSS background field equation (full gravitational self-force calculation, long-term)
13. Await Europa Clipper (2026-12-03) observational results — sealed prediction's P1 term coordinate frame confirmed correct

**Removed/superseded content:**
- Three earlier priority lists (dated 2026-06-26, 2026-06-27, 2026-06-28) have been marked outdated and removed, as some of their conclusions (e.g., the B_main=19,828km candidate value) have been overturned by the two-way Doppler analysis
- "Search for JUICE 2024 official analysis" is no longer necessary — the 2024 flyby altitude was too high (6,840 km), the framework already predicted no significant effect, and this research direction has been superseded by precise 2026 data
- The "whole-path weighting" direction for the fractional memory kernel (see the two toy model attempts under the Candidate 4 upgrade above) has been ruled out as an entire model class; Candidate 6 offers a structurally different alternative, to be prioritized over further fractional-calculus variants
- RQ2, RQ12 (in their original form) resolved/closed, moved out of the active priority list — see their respective sections

