# Yield analysis

## Primary point

At sigma_f = 97.57841384 MHz, collision-free yield is effectively near zero in both the spatial and shuffled cases. This operating point is therefore not used as a practical yield headline.

Its role is to test the primary scientific question at the measured-data-derived fabrication scale.

## Constant-q scale family

The original full sigma sweep keeps the fitted spatial covariance fraction q = 0.67549 fixed while changing total frequency spread.

At 10 MHz, the recovered exact yield values are:

- spatial collision-free yield = 92.584%
- shuffled collision-free yield = 54.200%
- yield advantage = +38.384 percentage points

This is a valid result for the constant-q scale family.

## Why the interpretation was revised

There are at least two distinct ways a lower total frequency spread might be reached:

1. **Process improvement:** correlated and local fabrication variation may shrink together. A roughly constant dimensionless q can be a useful modelling scenario.
2. **Individual post-fabrication tuning:** the original junction-resistance field is directly modified and additional prediction/tuning residuals can dominate. The final q can differ substantially from the pre-tuning q.

The project therefore does not map the constant-q 10 MHz result directly onto a real tuned processor without qualification.

## Residual-q sensitivity at 10 MHz

Recovered selected results:

| q | Spatial-minus-shuffled yield advantage |
|---:|---:|
| 0.05 | +1.87 pp |
| 0.10 | +4.09 pp |
| 0.20 | +8.45 pp |

These results establish that the practical yield effect varies continuously with retained spatial structure.

## Final yield conclusion

The project does not support the statement:

> Realistic 10 MHz processors gain 38 percentage points of yield from spatial correlation.

It supports the narrower statement:

> If the fitted Dolan spatial covariance fraction is preserved while total fabrication spread is reduced to 10 MHz, the frozen model predicts 92.584% spatial yield versus 54.200% shuffled yield.

For post-tuned processors, the size of the benefit remains conditional on the residual spatial covariance.
