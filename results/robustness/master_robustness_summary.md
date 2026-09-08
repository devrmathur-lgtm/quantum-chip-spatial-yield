# Master robustness summary

## Robust conclusions

- The primary paired spatial effect is negative: -5.02492 mean collisions.
- The primary effect is dominated by inter-site correlation rather than heterogeneous marginal variance.
- The sign of the primary spatial effect remains negative under all three audited Type-4 conventions.
- Selected low-sigma calculations show that yield advantage declines as retained q decreases.
- A small public LASIQ post-tuning residual map does not justify assuming the original pre-tuning q survives.

## Alternative covariance families retained

The project retained three alternative positive spatial covariance models at the primary 97.57841384 MHz scale:

- short-range stationary: a = 0.92842, r = 4.70596 mm
- dense NbTiN residual: a = 0.34266, r = 16.4246 mm
- weak all-Al residual: a = 0.04861, r = 14.7441 mm

Their exact original collision-output tables are not recoverable from the current file store. The scenario definitions are preserved in `spatial_model_scenarios.csv`, and the original output filenames are flagged for restoration in the audit folder.

## Other retained sensitivities

The final project also retained:

- physical-gradient scale-up sensitivity
- 60/70/80 MHz spacing sensitivity
- q lower-bound sensitivity
- constant-q full sigma sweep

These analyses support robustness but do not remove the major practical uncertainty: the covariance that remains after a real low-spread fabrication or tuning route.
