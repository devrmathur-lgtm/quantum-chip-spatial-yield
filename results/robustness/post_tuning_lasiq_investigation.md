# Post-tuning spatial-data investigation

The final audit looked for public data capable of constraining the spatial covariance that remains after individual qubit-frequency tuning.

A 27-qubit room-temperature LASIQ tuning-residual map was recoverable from public material.

Recovered diagnostics:

- RMS residual = 4.8668 MHz
- affine R^2 = 0.0112
- affine permutation p = 0.873
- nearest-neighbor correlation r = -0.155
- nearest-neighbor p = 0.492
- q-profile maximum-likelihood estimate = 0

This is not sufficient to conclude that cryogenic post-tuning q is zero. The dataset is small, room-temperature, and is not the same object as a full cryogenic post-tuning qubit-frequency residual map.

The scientifically correct conclusion is therefore:

> The actual spatial covariance remaining after modern individual post-fabrication tuning is unresolved by the public data examined.

That uncertainty is why low-spread yield results are reported as conditional scenarios.
