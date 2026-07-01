# Appendix — Data, Symbols, and Constants

**Last updated:** 2026-06-28 v1.4

---

## Symbol Table

| Symbol | Definition | Value / Unit |
|--------|------------|--------------|
| ΔV | Flyby velocity anomaly | mm/s |
| V∞ | Hyperbolic excess velocity | km/s |
| δᵢ | Inbound asymptote declination | degrees |
| δₒ | Outbound asymptote declination | degrees |
| δ_peri | Perigee geocentric declination | degrees |
| K | Anderson coefficient = 2ωR/c | 3.097 × 10⁻⁶ |
| ω | Earth rotation rate | 7.292115 × 10⁻⁵ rad/s |
| R | Earth mean radius | 6,371 km |
| c | Speed of light | 2.998 × 10⁸ m/s |
| G | Gravitational constant | 6.674 × 10⁻¹¹ m³/(kg·s²) |
| J_E | Earth angular momentum | 8.036 × 10³⁷ × ω kg·m²/s |
| B_main | Main field decay length | 16,076 km = 2.52 R_E |
| B_Busack | Busack secondary field decay length | 394 km |
| κ | Main field wavenumber = 1/B_main | 6.22 × 10⁻⁸ m⁻¹ |
| Ψ_bg | Background field | — |
| δΨ | Local perturbation field | — |
| A_φ | Gravitational vector potential (φ component) | m/s |
| P₁(cosδ) | Legendre polynomial l=1 | cosδ |
| P₂(cosδ) | Legendre polynomial l=2 | (3cos²δ − 1)/2 |
| ap | Geomagnetic planetary index | nT |
| F10.7 | Solar radio flux index | sfu |
| Lpp | Plasmapause L-shell | R_E |
| η | Volume integral amplification factor | 1.000 (no amplification) |

---

## Earth Constants

| Constant | Value |
|----------|-------|
| Mean radius R_E | 6,371.0 km |
| Mass M_E | 5.972 × 10²⁴ kg |
| Rotation rate ω_E | 7.292115 × 10⁻⁵ rad/s |
| Moment of inertia I_E | 8.036 × 10³⁷ kg·m² |
| Angular momentum J_E | 5.861 × 10³³ kg·m²/s |
| Average density ρ_E | 5,514 kg/m³ |
| GM_E | 3.986004 × 10⁵ km³/s² |

---

## LNSS Framework Constants

| Constant | Value | Derivation |
|----------|-------|------------|
| Anderson K | 3.097 × 10⁻⁶ | 2ω_E R_E/c |
| B_main | 16,076 km | Volume integral matching Anderson coefficient |
| B_Busack | 394 km | Busack (2007) empirical fit |
| κ_main | 6.22 × 10⁻⁸ m⁻¹ | 1/B_main |
| ρ_bg | 6.34 kg/m³ | ω_E²/(4πG) |
| v_p | 1,172 m/s | ω_E × B_main |
| \|P₂\|_c | ≈ 0.06 | Empirical (n=7) |
| c₂ (ap coefficient) | −0.249 mm/s/nT | Least-squares fit |

---

## Historical Flyby Data (complete)

| Flyby | Date | ΔV (mm/s) | δᵢ (°) | δₒ (°) | V∞ (km/s) | Alt (km) | ap | F10.7 | \|P₂(δ_peri)\| |
|-------|------|-----------|--------|--------|-----------|---------|-----|-------|----------------|
| Galileo I | 1990-12-08 | +3.92 | −12.52 | +34.26 | 8.949 | 960 | 8 | 223.6 | 0.165 |
| Galileo II | 1992-12-08 | −4.60 | −34.26 | −4.50 | 8.877 | 303 | 26 | 124.8 | 0.389 |
| NEAR | 1998-01-23 | +13.46 | −20.76 | +72.03 | 6.851 | 539 | 4 | 93.9 | 0.567 |
| Cassini | 1999-08-18 | −2.00 | −12.92 | −4.99 | 16.010 | 1172 | 28 | 133.9 | 0.091 |
| Rosetta I | 2005-03-04 | +1.82 | −2.81 | +34.29 | 3.863 | 1954 | 2 | 77.7 | 0.347 |
| Messenger | 2005-08-02 | ≈0.02 | +31.44 | −31.92 | 4.056 | 2347 | 1 | 93.5 | 0.036 |
| Juno | 2013-10-09 | 0.00 | −2.00 | −48.90 | 9.820 | 561 | 29 | 113.1 | 0.031 |

**Sealed predictions (2026-06-28):**

| Flyby | Date | δᵢ (°) | δₒ (°) | V∞ (km/s) | ΔV_P1 (mm/s) | \|P₂(δ_peri)\| |
|-------|------|--------|--------|-----------|-------------|----------------|
| JUICE | 2026-09-28/29 | −0.690 | +4.385 | 12.115 | +0.107 | 0.9991 |
| Europa Clipper | 2026-12-03 | +29.34 | +30.61 | 11.596 | +0.397 | 0.616 |

---

## P₂ Calm Zone

P₂(cosδ) = 0 at δ = ±arccos(1/√3) = **±54.7356°**

Effective "calm zone" with |P₂| < 0.06: **52.3° to 57.2°** (and −57.2° to −52.3°)

Width ≈ 5° centered on ±54.7°

---

## Key References

| Reference | Content |
|-----------|---------|
| Anderson et al. (2008), PRL 100, 091102 | Original flyby anomaly paper |
| Busack (2007) | Empirical fit including CMB direction |
| Carpenter & Anderson (1992) | Plasmapause position formula: Lpp = 5.7 − 0.47×Kp |
| NASA OMNIWeb | ap and F10.7 daily values |
| JPL Horizons | Spacecraft trajectory data (queried 2026-06-28) |
| Crespi et al. (2026), MNRAS | Fermionic dark matter core at Galactic Center |

---

## Data Sources

| Data type | Source | Query date |
|-----------|--------|------------|
| ap index (1990–2013) | NASA OMNIWeb OMNI2 daily | 2026-06-27 |
| F10.7 index (1990–2013) | NASA OMNIWeb OMNI2 daily | 2026-06-27 |
| JUICE trajectory (NAIF: −28) | JPL Horizons, Ecliptic J2000 | 2026-06-28 |
| Europa Clipper trajectory (NAIF: −159) | JPL Horizons, Ecliptic J2000 | 2026-06-28 |
| Earth trajectory (NAIF: 399) | JPL Horizons, Ecliptic J2000 | 2026-06-28 |

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| v1.0 | 2026-06-26 | Initial framework, 7-file structure |
| v1.1 | 2026-06-27 | NASA OMNIWeb data, three-body framework, Perturbation Model |
| v1.2 | 2026-06-27 | P₂ analysis, threshold hypothesis, sealed predictions |
| v1.3 | 2026-06-28 | Closed orbit theorem, GPS analysis, factor 2 (two-way Doppler), B_main plasmasphere validation |
| v1.4 | 2026-06-28 | JPL Horizons precise predictions (JUICE & Europa Clipper), English versions, GitHub preparation |
| v1.5 | 2026-06-28 | Bilingual publication (9 files × 2 languages), GitHub repo live, CC0 license, GitHub Release v1.0, Medium article published |
| v1.6 | 2026-06-30 | RQ4 methodological extension (inspired by Chen Lijie's paper), Candidate 4 (medium backreaction), Candidate 5 (nonlinear field coupling), fractional calculus toy model tests (both failed, recorded as negative results) |
| v1.7 | 2026-07-01 | Comprehensive review: fixed GitHub placeholder, consolidated 3 outdated priority lists into one, added OSIRIS-REx as 8th data point, discovered DSN tracking gap as literature support for Candidate 4, corrected oversimplified Juno framing in README |
| v1.8 | 2026-07-01 | Author byline corrected to Mao Lin Chang (across all files) |
| v1.9 | 2026-07-01 | Gravitational self-force (MiSaTaQuWa) as rigorous theoretical foundation for Candidate 4; real hyperbolic-orbit jerk calculation (third rejection of purely local instantaneous hypotheses); Candidate 6 (jump conditions / scattering framework) proposed and verified to reproduce the Anderson formula, questioning whether path integration is necessary |
| v1.10 | 2026-07-01 | Candidate 7 (topological classification): P₂'s exact node (54.7356°) divides declination into three regions; whether any of the trajectory's three characteristic angles ever leaves the equatorial band achieves 7/7 parameter-free classification; found to give an opposite prediction to the RQ14 |P₂| criterion for JUICE 2026, now recorded as an independent sealed prediction (original sealed content unmodified) |

---

## Known Differences Between Language Versions (honest disclosure)

- **The Chinese and English versions are not word-for-word translations.** English versions (`*_EN.md`) are condensed, focusing on core results, sealed predictions, and falsification conditions. The complete evolution of ideas (including superseded intermediate steps) exists only in the Chinese version. For the full derivation history, refer to the Chinese version.
- **04_Mathematics.md retains superseded analysis** (e.g., the "Factor 2 and B_main Coupling" section), marked as outdated but not deleted, to preserve a complete record of how ideas evolved. This is a deliberate design choice, not an oversight.
