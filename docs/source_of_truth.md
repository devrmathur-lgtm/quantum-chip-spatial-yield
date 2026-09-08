# Project source of truth

## Research question

Does preserving measured-data-derived spatial organization of fabrication-induced qubit-frequency errors change predicted frequency-collision statistics relative to an exact-value shuffled control?

The comparison is deliberately matched: the realized error values are held fixed and only their assignment to processor sites is changed.

## Primary experiment

- processor: 65-qubit distance-5 heavy-hex
- graph edges: 72
- nominal frequency groups: 5.00, 5.07, 5.14 GHz
- nominal spacing: 70 MHz
- anharmonicity: -330 MHz
- measured-data-derived total frequency spread: 97.57841384 MHz
- primary spatial covariance fraction: q = 0.67549
- primary paired Monte Carlo size: 100,000 realizations
- primary null: all-site exact-value shuffling
- no per-condition frequency-plan optimization

## Frozen primary result

Spatial mean collision burden: 14.10008

Shuffled mean collision burden: 19.12500

Paired spatial-minus-shuffled effect: -5.02492 collisions

Relative reduction: 26.27%

## Interpretation boundary

This result establishes a processor-level consequence of spatial organization under the specified model. It does not by itself establish that a future low-spread, post-tuned processor will preserve the same spatial covariance fraction.

The full sigma sweep with q held constant is a covariance-shape-preserving scaling experiment. It is not automatically a physical model of individual post-fabrication tuning.

## Final practical interpretation

At useful low spreads, the yield benefit depends on residual spatial covariance. The project therefore reports low-sigma results conditionally rather than asserting a universal practical yield gain.

## Novelty boundary

The project does not claim that:

- manufacturing variation exists,
- wafer variation can be spatially structured,
- covariance mathematics is novel,
- spatial manufacturing models have never been proposed for quantum-chip simulation.

The contribution tested here is the matched processor-level comparison between a measured-data-derived spatial model and an exact-value shuffled control under superconducting-qubit collision predicates.
