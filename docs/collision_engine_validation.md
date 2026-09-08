# Collision engine validation

## External benchmark

The collision architecture was benchmarked against:

J. B. Hertzberg et al., *Laser-annealing Josephson junctions for yielding scaled-up superconducting quantum processors*, npj Quantum Information 7, 129 (2021).

DOI: https://doi.org/10.1038/s41534-021-00464-5

The paper reports a distance-5 heavy-hex processor with 65 qubits, a three-frequency pattern around 5.00, 5.07, and 5.14 GHz, an anharmonicity of approximately -330 MHz, and a high-spread benchmark around 25 collisions at sigma_f = 132.3 MHz.

## Collision windows

The recovered Table-I tolerances are:

- Type 1: 17 MHz
- Type 2: 4 MHz
- Type 3: 30 MHz
- Type 4: directional architecture condition, no single tolerance in the original table
- Type 5: 17 MHz
- Type 6: 25 MHz
- Type 7: 17 MHz

## Type-4 ambiguity

Three Type-4 interpretations were audited:

1. later IBM/LASIQ symmetric convention
2. fixed-control one-sided Hertzberg interpretation
3. literal Hertzberg Table-I condition

At sigma_f = 132.3 MHz and 70 MHz nominal spacing, recovered benchmark totals were:

- symmetric: 24.7809
- one-sided: 24.0014
- literal: 44.3393

The symmetric and one-sided modes are both near the approximately 25-collision external benchmark. The benchmark alone therefore does not uniquely identify a single implementation.

## Production convention

The project retained the later IBM/LASIQ symmetric Type-4 convention as the frozen production mode.

The correct validation wording is:

> The heavy-hex architecture and collision engine are structurally tested and benchmark-matched under the later IBM/LASIQ Type-4 convention.

It would be too strong to claim that the historical Hertzberg implementation has been uniquely reconstructed from the benchmark alone.

## Primary Type-4 robustness

At 97.57841384 MHz:

- symmetric: spatial 14.1001, shuffled 19.1225, delta -5.0224
- literal Hertzberg: spatial 22.3292, shuffled 33.9147, delta -11.5855
- fixed-control one-sided: delta -4.7843, 95% CI [-4.8176, -4.7510]

The sign of the primary spatial effect remains negative under all three conventions tested.
