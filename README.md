# Spatial Fabrication Variation and Superconducting-Qubit Collision Yield

This repository studies whether the **spatial arrangement** of fabrication-induced qubit-frequency errors changes predicted frequency-collision statistics in a fixed-frequency superconducting processor, relative to a control that preserves the same realized error values but randomly shuffles their positions.

## Headline result

The preregistered primary experiment uses the measured-data-derived QuTech/Dolan spatial model at

- total frequency spread: **97.57841384 MHz**
- spatial covariance fraction: **q = 0.67549**
- processor: **65-qubit distance-5 heavy-hex**
- nominal frequency groups: **5.00, 5.07, and 5.14 GHz**
- nominal spacing: **70 MHz**
- anharmonicity: **-330 MHz**
- paired Monte Carlo realizations: **100,000**

Under that frozen model:

| Condition | Mean collisions |
|---|---:|
| Spatial assignment | 14.10008 |
| Exact-value shuffled assignment | 19.12500 |
| Spatial minus shuffled | -5.02492 |

This corresponds to a **26.27% lower mean collision burden** under the spatial assignment.

The scientifically firm conclusion is therefore:

> At the measured-data-derived fabrication scale, spatial assignment itself changes collision statistics even when the realized error values are held fixed.

At this high spread, collision-free processor yield is effectively near zero in both conditions, so this is a collision-burden result rather than a practical high-yield processor result.

## Low-spread engineering interpretation

The original constant-q scale-family experiment also found that, if the fitted pre-tuning spatial covariance fraction is preserved while the total frequency spread is reduced to 10 MHz, collision-free yield is approximately:

- **92.584% spatial**
- **54.200% shuffled**
- **+38.384 percentage points**

That result is mathematically valid **under the constant-q model**, but it must not be interpreted as an unconditional prediction for a real tuned processor.

A later q-by-sigma sensitivity analysis showed, at 10 MHz:

| q | Yield advantage |
|---:|---:|
| 0.05 | +1.87 pp |
| 0.10 | +4.09 pp |
| 0.20 | +8.45 pp |

The practical benefit therefore depends strongly on how much spatial covariance survives the physical route used to achieve lower frequency spread.

## Mechanism check

A decomposition of the 97.57841384 MHz primary effect found:

- IID equal-variance control: delta collisions = +0.00063
- heterogeneous diagonal-only covariance: delta collisions = -0.42270
- equal-marginal correlated covariance: delta collisions = -4.47699
- full primary covariance: delta collisions = -5.02492

A symmetric attribution assigns approximately **90.3%** of the primary effect to inter-site correlation and **9.7%** to heterogeneous site variances.

## Important repository status

This public-layout repository has been **reconstructed from the final project record**. The scientific conclusions and numerical headline results below are the final corrected values, but the original generated binary workbooks, full raw result arrays, and some original script bytes are not currently retrievable from the project file store.

For scientific integrity, missing original artifacts have **not** been fabricated. Their exact historical filenames and intended GitHub locations are listed in:

`docs/audit/original_artifacts_required.md`

The source code in `src/` is a clean public reference implementation of the frozen logic and controls. It is not claimed to be byte-identical to the archived working scripts.

## Repository structure

```text
.
├── README.md
├── RECONSTRUCTION_STATUS.md
├── requirements.txt
├── src/
├── tests/
├── data/
│   ├── raw/
│   └── processed/
├── results/
│   ├── primary/
│   ├── robustness/
│   └── figures/
└── docs/
    └── audit/
```

## Reproducing the analysis

The current repository can run unit tests for the collision predicates, exact-value shuffle control, and recovered model constants.

```bash
python -m unittest discover -s tests
```

Full raw-data-to-final-result reproduction requires restoration of the original QuTech/imec processed maps, 65-qubit coordinate/covariance data, and full Monte Carlo output arrays listed in `docs/audit/original_artifacts_required.md`.

## Scientific interpretation

The final evidence supports three distinct claims:

1. **Supported model claim:** spatial assignment itself changes collision statistics at fixed realized error values.
2. **Supported primary-model claim:** the frozen QuTech/Dolan model lowers mean collision burden by about 26% at 97.58 MHz.
3. **Conditional engineering claim:** at technologically useful spreads, the size of the yield benefit depends on the residual spatial covariance after process improvement or post-fabrication tuning.

The project does **not** claim that IID models are universally pessimistic, that spatial manufacturing models are a new concept, or that a real 10 MHz tuned processor necessarily receives a 38 percentage-point yield gain.

## Key literature

- J. B. Hertzberg et al., *Laser-annealing Josephson junctions for yielding scaled-up superconducting quantum processors*, npj Quantum Information 7, 129 (2021). https://doi.org/10.1038/s41534-021-00464-5
- Jacques Van Damme, *Scalable Superconducting Qubit Fabrication: A Study of Decoherence*, KU Leuven/imec PhD dissertation (2025).
- SPICE-Q (2026), manufacturing-aware quantum-chip simulation. The project treats this as prior work establishing that spatial manufacturing models can enter quantum-chip simulation, so no broader novelty claim is made.

## License

No license is included yet. Add one only after deciding how you want others to reuse the code and data.
