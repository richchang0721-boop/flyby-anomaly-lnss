# 06 — Falsification Conditions

**Last updated:** 2026-06-28 v1.4

---

## Core Principle

A good scientific hypothesis must specify what observations would cause it to fail.

---

## Observations That Would Immediately Falsify the LNSS Framework

| Condition | Consequence | Interpretation |
|-----------|-------------|----------------|
| Future coherent-tracking flyby (altitude < 2,000 km) shows no anomaly AND Anderson formula completely fails | Full framework failure | LNSS does not exist |
| Anderson formula error > 10 mm/s in any flyby, unexplained by P₂ or Busack terms | Major revision required | Framework incomplete |
| Juno's zero result fully explained by gravitational model errors (GRACE correction exactly +10.4 mm/s) | LNSS explanation excluded | Shift to gravitational modeling error hypothesis |

---

## Observations That Would Falsify the P₂ Calm-Zone Hypothesis

| Condition | Interpretation |
|-----------|----------------|
| Future flyby with perigee at 50°–58° shows significant anomaly (> 2 mm/s) | P₂ node is not the cause of null results |
| Flyby with perigee far from ±54.7° (e.g., 30°) produces a null result | P₂ is not the decisive feature |

---

## Observations That Would Falsify the Solar Wind Compression Hypothesis

| Condition | Interpretation |
|-----------|----------------|
| Low-altitude flyby during solar maximum shows normal (nonzero) anomaly | Solar wind does not suppress LNSS |
| Precise correlation r(F10.7, \|dV\|) ≈ 0 | Solar activity is not the relevant variable |

---

## Observations That Would Support the LNSS Framework

| Condition | Support strength |
|-----------|-----------------|
| Europa Clipper 2026: precise model analysis still shows anomaly > 1 mm/s | Strong |
| Future flyby at perigee ≈ ±39.2° (P₃ node) shows smaller residual than Anderson | Medium |
| n > 10 flybys confirm \|P₂\|_c threshold separates null and anomalous cases | Strong |
| Any closed orbit (LEO/GPS) continues to show zero Anderson-type anomaly | Strong (ongoing confirmation) |

---

## Non-Falsifiable Parts (Weaknesses)

The following aspects of the framework **cannot currently be tested by any direct observation** — this is an acknowledged weakness:

1. **Physical nature of the background field Ψ_bg** — what medium? what field equation?
2. **Theoretical origin of κ = 1/B_main** — why this particular wavenumber?
3. **Orbital drift effects** — predicted magnitude too small to measure currently

Improvement direction: formalize these concepts into calculable quantities with specific numerical predictions.

---

## Closed Orbit Zero Result: Strong Consistency Verification (added 2026-06-28)

**Mathematical theorem (proven):** The Anderson effect is exactly zero for any closed orbit.

```
ΔV = V∞ · K · (cosδᵢ − cosδₒ)
Closed orbit: δᵢ = δₒ  →  ΔV ≡ 0  (exact, topological)
```

ISS verification (inclination 51.6°): ∫sinδ dδ summed over four orbital segments = 0.000000 (exact).

**GPS analysis (2026-06-28):**

| Effect | Magnitude | Conclusion |
|--------|-----------|------------|
| Anderson path integral | **≡ 0 (exact)** | Topological protection of closed orbits |
| LNSS equivalent continuous acceleration | ~3×10⁻⁸ m/s² | Below SRP error floor (10⁻⁷ m/s²) |
| GPS SLR residual precision | 2–4 cm; dominated by SRP | LNSS signal buried, cannot be isolated |

**Key insight:**
- GPS showing no LNSS signal is **support for the framework, not a refutation**
- The framework's design (path integral effect) makes it observable only in open hyperbolic trajectories
- LEO, GPS, Starlink, ISS, space debris — all closed orbits are topologically protected

**Status update:** "Closed orbits show no Anderson effect" has been upgraded from "problem to explain" to "framework prediction verified."

---

## Updated Falsification Summary

| Condition | If true, then |
|-----------|---------------|
| Closed orbit (LEO/GPS) exhibits Anderson-type anomaly | Framework entirely fails |
| Open hyperbolic flyby deviates from Anderson formula geometry | Framework entirely fails |
| Europa Clipper 2026: precise model gives ΔV = 0 (perigee not near P₂ node) | Major revision required |
| n > 10 flybys: ap–dV correlation disappears | ap effect is coincidental |
| Future flyby near P₂ node (±54.7°) shows significant anomaly | P₂ hypothesis fails |
| JUICE 2026 or Europa Clipper 2026: \|ΔV\| > 3 mm/s | Outside all framework parameters |
