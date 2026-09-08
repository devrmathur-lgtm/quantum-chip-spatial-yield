# Research and methods

## 1. Fabrication data and frequency conversion

The spatial model was derived from public QuTech/imec Josephson-junction fabrication data associated with the Planar-17 layout.

The reconstruction used:

- 17 physical positions
- approximately 2.308 mm average physical pitch
- 113 complete Dolan maps
- 51 paper-filtered Manhattan maps
- measured-data-derived Dolan frequency spread of 97.57841384 MHz

The resistance-to-frequency mapping used the transmon-style relationship

\[
f_{01} = \sqrt{8 f_C M G} - f_C
\]

with

- \(f_C = 270\) MHz
- \(M = 134\) GHz/mS

The reconstructed frequency spreads were approximately 97.58 MHz for the Dolan data and 154.76 MHz for the Manhattan comparison.

## 2. Spatial characterization

The final affine spatial model was fit before the primary collision experiment was evaluated.

Recovered diagnostics for the transferred 65-qubit covariance include:

- primary q = 0.67549
- lower fitted q bound = 0.4852
- minimum site variance = 0.3245 sigma^2
- maximum site variance = 1.9492 sigma^2
- mean adjacent-site correlation = 0.5718
- mean adjacent-difference variance = 0.68865 sigma^2

The model therefore contains both off-diagonal correlation and position-dependent marginal variance.

## 3. Processor geometry

The target processor is an exact distance-5 heavy-hex reconstruction with:

- 65 qubits
- 72 coupling edges
- three nominal frequency groups at 5.00, 5.07, and 5.14 GHz
- 35 degree-two controls assigned to the high nominal frequency group in the frozen plan

The frequency plan is identical in the spatial and shuffled conditions.

## 4. Collision engine

Collision Types 1 to 7 follow the frequency-collision structure in Hertzberg et al. The production Type-4 interpretation was the later IBM/LASIQ symmetric convention, and two alternative interpretations were subsequently audited.

The external benchmark used the 132.3 MHz fabrication-spread case reported in Hertzberg et al.

## 5. Paired spatial-versus-shuffled experiment

For each realization:

1. Generate one set of frequency-error values under the frozen spatial model.
2. Evaluate collisions with those values assigned to their spatially generated sites.
3. Randomly permute the same realized values across sites.
4. Evaluate collisions again using the same graph, nominal frequencies, and collision rules.
5. Record the paired spatial-minus-shuffled difference.

This exact-value shuffle isolates assignment effects from the marginal realized error multiset.

## 6. Primary endpoint

The preregistered primary endpoint is mean total collision count at 97.57841384 MHz.

Primary result:

- spatial = 14.10008
- shuffled = 19.12500
- delta = -5.02492
- reduction = 26.27%

## 7. Robustness analyses

The later audit added or retained:

- q uncertainty and alternative covariance-family tests
- physical-gradient scale-up sensitivity
- 60/70/80 MHz frequency-plan spacing sensitivity
- three Type-4 conventions
- heteroscedasticity-versus-correlation decomposition
- low-sigma q sensitivity
- post-tuning residual-data investigation

The final interpretation separates the primary measured-data result from conditional low-spread engineering scenarios.
