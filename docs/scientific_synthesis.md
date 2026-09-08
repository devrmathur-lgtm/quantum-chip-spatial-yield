# Scientific synthesis

## Main finding

The central controlled result is that the spatial assignment of fabrication-derived qubit-frequency errors affects collision statistics even when the realized error values themselves are held fixed.

At the measured-data-derived scale of 97.57841384 MHz, the frozen QuTech/Dolan model gives:

- spatial mean collisions: 14.10008
- shuffled mean collisions: 19.12500
- paired effect: -5.02492 collisions
- relative reduction: 26.27%

This is the highest-confidence project result because the fabrication-amplitude scale and spatial model are both tied to the same measured-data analysis and the comparison is paired.

## Why the effect occurs

For two sites \(i,j\),

\[
\mathrm{Var}(f_i-f_j)
=
\mathrm{Var}(f_i)
+
\mathrm{Var}(f_j)
-
2\,\mathrm{Cov}(f_i,f_j).
\]

Positive covariance can therefore narrow relative-frequency differences for nearby sites. Collision predicates depend on frequency differences and combinations, so changing the covariance structure changes the probability of entering collision windows.

The primary decomposition shows that this mechanism is not mainly an artifact of heterogeneous site variances. Approximately 90.3% of the primary effect is attributed to inter-site correlation under the symmetric decomposition.

## What the high-spread result does and does not mean

At 97.58 MHz, collision-free yield is effectively unresolved near zero in both conditions. The primary result is therefore best understood as a causal/model demonstration about collision burden, not a claim that a useful high-yield processor exists at that spread.

## Low-spread engineering scenarios

A constant-q scale-family calculation gives 92.584% spatial versus 54.200% shuffled collision-free yield at 10 MHz, a +38.384 percentage-point difference.

That number is conditional. It assumes the original q = 0.67549 covariance fraction survives while the total frequency spread shrinks.

The later sensitivity analysis demonstrates the dependence explicitly. At 10 MHz:

- q = 0.05 gives +1.87 percentage points
- q = 0.10 gives +4.09 percentage points
- q = 0.20 gives +8.45 percentage points

The engineering question therefore becomes: how much spatial covariance survives process improvement or individual tuning?

## Post-tuning uncertainty

A public 27-qubit room-temperature LASIQ tuning-residual map gave:

- RMS residual = 4.8668 MHz
- affine R^2 = 0.0112
- affine permutation p = 0.873
- nearest-neighbor r = -0.155
- nearest-neighbor p = 0.492
- q-profile MLE = 0

This small room-temperature map does not establish the cryogenic post-tuning covariance of a future processor. It instead supports treating post-tuning q as unresolved.

## Final claims

Supported:

1. Spatial assignment changes collision statistics at fixed realized error values in the frozen model.
2. The measured-data-derived primary model reduces mean collision burden by about 26% at 97.58 MHz.
3. Inter-site correlation dominates the primary effect relative to sitewise heteroscedasticity.

Conditional:

4. Large low-spread yield advantages are possible if substantial spatial covariance is retained.

Unresolved:

5. The spatial covariance that survives modern individual post-fabrication tuning.

Unsupported:

6. A universal claim that IID models are pessimistic.
7. A claim that every real 10 MHz processor receives a 38 percentage-point yield improvement.
8. A claim that the general idea of spatial manufacturing-aware quantum-chip simulation is new.
