<div align="center">

# LNSS / Perturbation Model — Earth Flyby Anomaly Research

**Language: [English](README.md) | [繁體中文](README_ZH.md)**

*An independent research project on the Earth flyby anomaly — unexplained mm/s-scale velocity discrepancies observed in hyperbolic spacecraft trajectories past Earth.*

</div>

---

## What This Is

Since 1990, several spacecraft performing gravity-assist flybys of Earth (Galileo, NEAR, Cassini, Rosetta, MESSENGER, Juno) have shown small (mm/s-scale) unexplained velocity anomalies relative to standard orbital mechanics predictions — the **Anderson flyby anomaly** (Anderson et al. 2008, PRL). This repository documents an independent research effort to explain the anomaly through a minimal extension of known physics (the **LNSS / Perturbation Model** framework), using a background field perturbed by Earth's rotation.

This is **independent research**, not peer-reviewed publication. Results, including negative results and past mistakes, are documented transparently — see [CHANGELOG.md](CHANGELOG.md) for a running record of what was found, revised, and overturned, and why.

## Author

Mao Lin Chang, in collaboration with GPT (OpenAI) and Claude (Anthropic) as research-assistant tools. See [Methodology & AI Involvement](#methodology--ai-involvement) below for how AI tools were used and what safeguards were put in place.

---

## Current Status (2026-07-03)

**Established, high-confidence results:**
- **Closed-orbit topological theorem:** ΔV ≡ 0 exactly for any closed orbit (proven, verified against ISS/GPS geometry) — the framework's strongest result.
- **Anderson formula's factor of 2** traced to two-way Doppler tracking methodology, with a quantified bound (O(v²/c²) ~ 10⁻⁹) showing the outbound/return-leg asymmetry is negligible.
- **Anderson P₁ formula** (ΔV = V∞·(2ωR/c)·(cosδᵢ−cosδₒ)) validated against 6 of 7 reconstructed historical flybys to within ~0.2 mm/s using JPL Horizons–derived trajectory angles (see [Reproducible Calculation Pipeline](#reproducible-calculation-pipeline)).

**Overturned as of 2026-07-02 (see CHANGELOG.md for full detail):**
- The historical δ_peri (perigee declination) values used throughout early versions of this framework had no documented derivation and were found to be physically inconsistent (e.g., Galileo I's old value exceeded the declination bound implied by its own orbital inclination). Full reconstruction from JPL Horizons raw vectors overturned:
  - **Candidate 7** (topological node classification, "7/7 accuracy") — δ_peri contributed zero correct classifications across all 7 reconstructed flybys.
  - **The |P₂(cosδ_peri)| vs |ΔV| correlation (r=0.852)**, which had been the framework's central "geometry is dominant" claim — could not be reproduced with corrected δ_peri (position-based: r=+0.082, null; velocity-based: r=−0.863, opposite sign, borderline significance).
  - **Juno's own δᵢ, δₒ** (not just δ_peri) were also found to be wrong; corrected values match independent literature (Jouannic et al. 2015; Acedo 2017) almost exactly. Juno's "unexplained P₁ prediction" is corrected from the previously stated +10.4 mm/s to ~6.0–6.3 mm/s.

**Open problems:**
- **RQ4:** Why Juno's observed ΔV is zero despite a nonzero Anderson P₁ prediction (~6 mm/s) — still unresolved.
- **RQ12:** The physical origin of κ = 1/B_main (B_main = 16,076 km) — cannot be derived from Earth-local constants (exhaustive dimensional analysis); reframed as a framework free parameter, tentatively supported as an intrinsic background-field property rather than locally modulated (see 07_Open_Problems.md).
- δ_peri's correct definition (position vs. velocity declination) remains undetermined.

**Upcoming falsifiable tests:**
- **JUICE flyby, 2026-09-28/29** and **Europa Clipper flyby, 2026-12-03** — sealed predictions in `05_Predictions.md`, written before the observations, not to be modified afterward.

---

## Repository Structure

```
LNSS/
├── README.md / README_ZH.md          ← you are here
├── 01_Observations.md                ← flyby data, reconstructed geometry, solar activity
├── 02_Constraints.md                 ← what any valid theory must satisfy
├── 03_Hypotheses.md                  ← the Perturbation Model, candidate mechanisms
├── 04_Mathematics.md                 ← derivations: Anderson formula, closed-orbit theorem, etc.
├── 05_Predictions.md                 ← sealed predictions for upcoming flybys (immutable once sealed)
├── 06_Falsification.md               ← what observations would refute this framework
├── 07_Open_Problems.md               ← research questions, candidate mechanisms, current priorities
├── Appendix_Data.md                  ← constants, symbols, full historical data table, references
├── CHANGELOG.md                      ← dated record of what changed and why (including corrections)
├── EN/                               ← English translations of all documents above
├── constants.py                      ← single source of truth for physical constants
├── reconstruct.py                    ← reconstructs flyby geometry from raw JPL Horizons data
├── validation_tests.py               ← automated sanity checks (see below)
├── results.json                      ← single source of truth for reconstructed numerical values
└── data/
    ├── raw/                          ← original JPL Horizons query outputs (immutable)
    └── processed/                    ← parsed intermediate data
```

**Note on language versions:** English files are more condensed, focused on core results, sealed predictions, and falsification conditions. The Traditional Chinese version (root-level `.md` files) contains the complete evolution of ideas, including superseded intermediate steps and the full audit trail — it is the primary working language of this research. For the complete derivation history, refer to the Chinese version.

---

## Reproducible Calculation Pipeline

A significant methodological finding of this project (2026-07-02) is documented in `CHANGELOG.md`: numerical values that exist only as LLM-generated text, without a traceable computational origin, cannot be trusted — even after being repeatedly reused across weeks of analysis. In response, all trajectory-derived numbers now follow a fixed pipeline:

```
data/raw/*.txt  (JPL Horizons, equatorial/ICRF frame, geocentric, 1-minute step)
      ↓
reconstruct.py   (finds precise perigee, computes position & velocity declination)
      ↓
validation_tests.py   (automated checks: altitude vs. official value, inclination bound, etc.)
      ↓
results.json   (the only authoritative source for δᵢ, δₒ, δ_peri, perigee altitude, etc.)
```

**Rule for anyone (human or AI) reviewing this research:** trajectory-derived numerical claims should be checked against `results.json`, or reproduced by rerunning `reconstruct.py` against the raw data in `data/raw/`. They should not be regenerated from memory or re-derived from natural-language reasoning alone.

To reproduce:
```bash
python3 reconstruct.py data/raw/Galileo01_horizons_results_min.txt 960
python3 validation_tests.py results.json
```

---

## Methodology & AI Involvement

This research was conducted collaboratively between the author and two AI systems (GPT and Claude), used as reasoning and calculation-execution assistants — not as sources of unverified factual claims. A key lesson learned mid-project (documented in `CHANGELOG.md`) is that LLM-generated numerical results, even when repeatedly reused and seemingly consistent, can share undetected errors, because different models and sessions do not reliably catch each other's blind spots through text-based cross-review alone.

The working principle adopted going forward:

> **AI may participate in reasoning, but should not be the origin of factual claims.**

Concretely: any number describing physical reality should be traceable to an external, executable source (e.g., a JPL Horizons query run through `reconstruct.py`), not to a piece of LLM-generated prose. Cross-model discussion (Claude/GPT) is used to generate hypotheses and surface blind spots, not to validate truth by consensus.

---

## License

Data and text in this repository are released under CC0 (public domain dedication) unless otherwise noted.

## Key References

- Anderson, J. D. et al. (2008). "Anomalous Orbital-Energy Changes Observed during Spacecraft Flybys of Earth." *Phys. Rev. Lett.* 100, 091102.
- Busack, H.-J. (2007, 2013). Alternative empirical fit including CMB-direction asymmetry term.
- Jouannic, B. et al. (2015). Flyby anomaly compilation and analysis, ISSFD.
- Acedo, L. (2017). Literature review of flyby anomaly theories. arXiv:1701.05735.
- Thompson, P. F. et al. (2014). Juno Earth flyby tracking analysis.
