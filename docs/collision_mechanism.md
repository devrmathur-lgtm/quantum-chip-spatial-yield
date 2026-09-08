# Collision mechanism analysis

## Relative-frequency covariance

Collision conditions depend on frequency differences and sums. For a pair of sites,

\[
\mathrm{Var}(f_i-f_j)
=
\mathrm{Var}(f_i)+\mathrm{Var}(f_j)-2\mathrm{Cov}(f_i,f_j).
\]

Positive inter-site covariance can narrow the distribution of pairwise differences. Because the heavy-hex collision rules are not all simple pairwise equal-frequency windows, individual collision categories can move in different directions even when total collision burden falls.

## Primary decomposition

At 97.57841384 MHz:

| Covariance construction | Spatial minus shuffled mean collisions |
|---|---:|
| IID equal variance | +0.00063 |
| Heterogeneous diagonal only | -0.42270 |
| Equal-marginal correlated | -4.47699 |
| Full primary covariance | -5.02492 |

The diagonal-only contribution has about 8.41% of the full effect magnitude when compared directly.

A symmetric attribution gives approximately:

- 9.7% heteroscedasticity
- 90.3% inter-site correlation

This supports the interpretation that genuine inter-site covariance, rather than only site-dependent marginal spread, drives most of the primary collision reduction.

## Low-spread decomposition

At 10 MHz:

| Case | Delta collisions | Yield advantage |
|---|---:|---:|
| IID | +0.0026 | -0.13 pp |
| Heterogeneous diagonal only | -0.0667 | +2.96 pp |
| Equal-marginal correlated | -0.5808 | +30.42 pp |
| Full primary | -0.6899 | +38.24 pp |

At 14 MHz, recovered yield advantages are:

- heterogeneous diagonal only: +0.85 pp
- equal-marginal correlated: +26.07 pp
- full primary: +33.73 pp

The symmetric attribution at 14 MHz assigns about 87.4% of the effect to correlation and 12.6% to heteroscedasticity.

## Scope

These mechanism conclusions are statements about the specified covariance models. They do not prove that a future post-tuned processor retains the same covariance.
