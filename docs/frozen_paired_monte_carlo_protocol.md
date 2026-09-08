# Frozen paired Monte Carlo protocol

## Primary purpose

Measure the effect of **spatial assignment** while holding the realized set of fabrication-error values fixed.

## Pair construction

For each Monte Carlo realization:

1. Draw one 65-site frequency-error vector from the frozen spatial model.
2. Add it to the fixed nominal 65-qubit frequency plan.
3. Count collisions using the frozen collision engine.
4. Randomly permute the exact same 65 error values across the 65 sites.
5. Add the permuted values to the identical nominal frequency plan.
6. Count collisions again.
7. Save the paired difference: spatial minus shuffled.

The primary null is therefore an all-site exact-value shuffle, not an independently resampled IID population.

## Primary scale

- sigma_f = 97.57841384 MHz
- q = 0.67549
- realizations = 100,000

## Frozen endpoint

Mean total collision count and the paired spatial-minus-shuffled difference.

## Important constraints

- same graph in both conditions
- same nominal frequencies in both conditions
- same collision rules in both conditions
- same realized error multiset within each pair
- no condition-specific frequency optimization

The archived original RNG seed and full realization arrays are not available in the current reconstructed package. A public reference implementation is provided in `src/paired_monte_carlo.py`.
