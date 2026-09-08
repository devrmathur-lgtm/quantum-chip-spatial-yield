# Heteroscedasticity and correlation decomposition

The transferred affine covariance contains both:

1. position-dependent marginal variances
2. inter-site covariance

The decomposition isolates these effects.

At 97.57841384 MHz:

- IID: +0.00063 collisions
- heterogeneous diagonal only: -0.42270
- equal-marginal correlated: -4.47699
- full primary: -5.02492

The direct diagonal-only magnitude is about 8.41% of the full effect.

Using the symmetric attribution adopted in the final project:

- heteroscedasticity: approximately 9.7%
- inter-site correlation: approximately 90.3%

At 14 MHz, the corresponding symmetric attribution is approximately 12.6% heteroscedasticity and 87.4% correlation.

The conclusion is that off-diagonal spatial correlation is the dominant driver of the primary effect, while heterogeneous marginal variance makes a smaller but nonzero contribution.
