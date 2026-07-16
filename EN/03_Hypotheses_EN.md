# 03 — Hypotheses

**Last updated:** 2026-07-14 v1.6 (added citation check: Einstein's 1920 Leiden address cannot support Ψ_bg)

---

## Core Framework: Perturbation Model

### Conceptual Shift (2026-06-27)

**Previous (Source Model):** Earth's rotation creates LNSS; far-field boundary Ψ → 0

**Current (Perturbation Model):** A cosmic background field Ψ_bg exists; Earth merely perturbs it locally

```
Cosmic background field Ψ_bg  (uniform; direction determined by CMB dipole)
        ↓  Earth mass + rotation → local perturbation
        ↓  Forms P₁/P₂ local modes  (sinθ structure from GR)
        ↓  Solar wind (ap) modulates amplitude  (secondary)
        ↓  Earth flyby anomaly ΔV
```

**Three previously puzzling facts resolved by this model:**

| Puzzle | Resolution |
|--------|------------|
| Physical origin of k² | Background field curvature — no new particles needed |
| Busack's CMB direction | Preferred direction of background field, enters far-field boundary condition naturally |
| Anderson formula has no altitude term | Main field decay length B_main >> all flyby altitudes; field nearly constant across 300–2000 km |

---

## Two Decay Length Scales

```
Anderson main field (δΨ_P₁):  B_main = 16,076 km  (2.52 R_E)
                                → No altitude correction in Anderson formula ✓

Busack secondary field (δΨ_CMB): B_Busack = 394 km
                                → Busack formula's B parameter ✓
```

Both scales correspond to known geophysical length scales — neither is a free parameter in isolation.

---

## Background Field Properties

From the Anderson coefficient, the background field must satisfy:

```
Wavenumber:       k = 1/B_main = 6.22 × 10⁻⁸ m⁻¹
Wavelength:       λ = 2π/k ≈ 101,000 km ≈ 15.9 R_E
Equivalent density: ρ_bg = ω_E²/(4πG) = 6.34 kg/m³
Wave phase speed: v_p = ω_E × B_main = 1,172 m/s
```

This density (6.34 kg/m³) is 870× less than Earth's average density, but 22 orders of magnitude greater than any known cosmic background medium. It may represent a locally bound state in Earth's gravitational field.

---

## Excluded Hypotheses

The following have been quantitatively excluded:

| Hypothesis | Exclusion basis |
|-----------|-----------------|
| Solar wind truncation of plasmasphere | Lpp always outside B_main (calculated from Carpenter & Anderson 1992 formula) |
| 7.3× amplification mechanism | Spurious — full volume integral gives η = 1 |
| Plasma coupling explaining B = 394 km | No matching plasma scale exists |
| Multipole expansion (P₁+P₂+P₃) explaining Juno | Coefficients unphysical (large magnitude, alternating signs); overfitting (n=7, 4 parameters) |
| Space debris angular momentum as "bridge pier" | 10¹⁶× smaller than Earth's angular momentum |
| Dark energy direct effect | Characteristic length ~5,300 Gpc — 10⁴⁰× wrong scale |
| F layer ionosphere as k² source | No plasma scale corresponds to 394 km |
| v × B_g type magnetic force | Force direction is φ̂ ⊥ velocity; cannot change speed magnitude |

---

## Dark Matter + Plasma Compound Medium Hypothesis (RQ11)

**Proposed by Rich Chang (2026-06-28):**

The background field wave number k = 1/B_main may arise from an interaction between the cosmic dark matter/dark energy background and the local plasma environment near Earth.

**Calculation results:**

| Candidate | Characteristic length | vs B_main | Conclusion |
|-----------|----------------------|-----------|------------|
| Dark energy (Λ) | ~5,300 Gpc | 10⁴⁰× too large | ✗ |
| Local dark matter (CDM) | ~10⁶ km | **~100× too large** | △ Closest candidate |
| Plasma + dark matter coupling | ~5 m (plasma-dominated) | Far off | ✗ |
| Jeans instability (ρ_bg = 6.34 kg/m³) | = B_main | = 1 | △ Self-consistent but origin unclear |

**The "factor of 100" gap:** Local dark matter density gives a characteristic length ~10⁶ km, approximately 100× larger than B_main. If a mechanism existed to locally concentrate dark matter by ~100× in Earth's vicinity, the gap would close. This is not a random large number — it is potentially meaningful.

**Hypothesis grade: ★☆☆☆☆ (Conceptual — no direct calculation support)**

---

## Hypothesis: Excitable Medium as the Source of P₂/P₃ Correction Terms (2026-07-03)

**Background:** An extension of the Kármán vortex street analogy (see the Chinese version, 03_Hypotheses.md, for the full vortex-street discussion) into a mathematically well-defined nonlinear-dynamics framework. Excitable media are a real, established scientific concept (FitzHugh-Nagumo model, Belousov-Zhabotinsky chemical oscillations, cardiac tissue electrical propagation are standard examples) — not a borrowed term from an unrelated field.

**Defining features (all required):**
1. Threshold behavior: below threshold, perturbations decay naturally; above threshold, triggers an **all-or-none** response of fixed strength
2. Refractory period: after firing, the medium needs recovery time, during which further stimulation produces no response
3. Propagation is a traveling wave at a fixed speed, not instantaneous field superposition

**Structural tension with the framework's established results (recorded honestly, not avoided):**

- **The Anderson formula (P₁ main term) is smooth and linear** — ΔV ∝ V∞ ∝ (cosδᵢ−cosδₒ), varying continuously — directly at odds with an "all-or-none" threshold response.
- **The closed-orbit topological theorem** (★★★★★, the framework's strongest result) is proven via linear superposition of sinδ integrating to zero; a nonlinear excitable-medium system offers no guarantee of this clean cancellation.

**A narrowed, potentially viable scope:** Keep P₁ on the existing linear GEM mechanism (now established via the GEM derivation, see 07_Open_Problems_EN.md "GEM derivation establishes A₂=0"), and restrict the excitable-medium idea to **P₂/P₃-type secondary corrections only**. This narrowed scope happens to fill an existing gap: the GEM derivation already showed A₂'s theoretical value is zero, meaning any real P₂ effect must come from "a mechanism outside the framework" — and excitable media are currently the only concretely proposed, mathematically well-defined candidate for that outside mechanism.

**An untested but theoretically implied new falsifiable prediction:** If the excitable-medium hypothesis holds, the "refractory period" feature predicts that two flybys close together in time should show a weakened second signal (the medium still recovering). All 7 historical cases are years apart — this prediction has never been tested and there is currently no opportunity to test it; recorded as a condition that could be checked against a future closely-spaced flyby schedule.

**Hypothesis grade: ★☆☆☆☆ (Conceptual, same tier as the Kármán vortex analogy; scope narrowed to P₂/P₃ to avoid conflict with the linear P₁ formula and the closed-orbit theorem)**

---

## External Related Hypotheses (2026-06-28)

### E1: Galactic Center as Fermionic Dark Matter Core (Crespi et al. 2026)

**Source:** Valentina Crespi et al., MNRAS 2026. "The dynamics of S-stars and G-sources orbiting a supermassive compact object made of fermionic dark matter."

**Core claim:** The Milky Way's Sgr A* may not be a supermassive black hole, but a dense core of self-gravitating fermionic dark matter (the RAR model: Ruffini-Argüelles-Rueda). This model can explain S-star orbits, G-cloud behavior, and even the Event Horizon Telescope shadow image.

Fermion mass estimate: ~10–100 keV/c²

**Relevance to LNSS:**

| Aspect | Assessment |
|--------|------------|
| Direct impact | Low — galactic center is 10²⁰× larger than B_main |
| Indirect impact | If confirmed, galactic dark matter distribution needs recalculation; local DM density may change |
| Particle mass scale | ~50 keV/c² behaves as classical particle at B_main scales (de Broglie wavelength ~0.4 nm) |

**Notable:** If future observations confirm a fermionic dark matter core and the resulting local DM density revision approaches the "factor of 100" gap in RQ11, the coincidence would become significant.

**Hypothesis grade: ★☆☆☆☆ (externally related; no direct calculation support)**

### E2: Dark Energy is Weakening (DESI 2024–2026)

**Source:** DESI Collaboration 2024; multiple independent analyses 2025–2026.

**Core claim:** The cosmological constant Λ may not be constant. DESI data suggests dark energy strength may be declining over cosmic time.

**Relevance to LNSS:** Dark energy decay does not affect B_main calculations — Λ's characteristic length scale is Gpc (10⁴⁰× too large, confirmed excluded in RQ11). However, if dark energy is a dynamic field (quintessence) rather than a constant, it could have spatial variations at sub-cosmological scales. This is a conceptual avenue worth tracking.

**Hypothesis grade: ★☆☆☆☆ (externally related; scale mismatch too large)**

---

### 🆕 Citation Check: Einstein's 1920 Leiden Address Cannot Support Ψ_bg (2026-07-14)

**Note on nature of this entry: not a new hypothesis, but a citation-verification record — to prevent this common misreading from being cited again in the future.**

**A commonly cited claim:**
> "According to the general theory of relativity, space without ether is unthinkable" — Albert Einstein, inaugural address at the University of Leiden, May 5, 1920, "Ether and the Theory of Relativity"

**Verification result: the quote is accurate verbatim, but the very next sentence excludes the property Ψ_bg needs:**

> "But this ether may not be thought of as endowed with the quality characteristic of ponderable media, as consisting of parts which may be tracked through time. **The idea of motion may not be applied to it.**"

**The core mismatch: Einstein's "ether" = the general-relativistic metric field g_μν itself, with no independent dynamics, no trackable motion, no state of its own. This is the opposite of what Ψ_bg requires — an intrinsic characteristic length (B_main), local perturbability by Earth's rotation, and possibly a preferred CMB-dipole direction. Einstein explicitly excludes exactly the properties Ψ_bg structurally requires.**

**Modern scholarly consensus (cited):**
> "Einstein referred to the metric field g_μν itself—varying from place to place, determined by material phenomena, and never assignable to an independent state of motion...the ether that Einstein reintroduced differed fundamentally from the ether he had banished."
> — from a commentary on the Weinstein controversy (arXiv:2510.03793, 2025)

In other words: this lecture was a deliberate rhetorical repurposing of the word "ether" to mean "spacetime itself has physical qualities," not the reintroduction of an independent medium with its own dynamics that could be locally perturbed.

**Disposition: this does not exclude the Ψ_bg concept itself** (background-field concepts remain fully legitimate in modern physics — see the dark energy/quintessence/Higgs-field discussion in section E2 above) — **it only excludes citing Einstein's 1920 lecture as physical support for Ψ_bg's existence.** This is a widely-circulated case of quoting only the first sentence while dropping the qualifying clause that follows; not an error specific to this framework, but worth recording to prevent reuse.
