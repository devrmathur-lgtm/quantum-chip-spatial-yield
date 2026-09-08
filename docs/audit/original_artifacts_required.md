# Original artifacts still required for complete reproduction

These files were part of the authoritative project history but are not available as byte-retrievable artifacts in the current project file store.

They have deliberately **not** been synthesized from incomplete information.

## Raw and processed spatial data

Target these under `data/raw/` or `data/processed/` when recovered:

- `imec_step1_clean_map.xlsx`
- `imec_JV_cleaned_long.csv`
- `qutech_spatial_characterization_final.xlsx`
- `qutech_spatial_map_and_heavyhex_geometry.xlsx`
- `qutech_planar17_coordinates.csv`
- `qutech_die_averaged_maps.csv`
- `spatial_model_fit_results.csv`
- `spatial_model_validation.csv`
- `affine_detrending_check.csv`
- `spatial_model_65q_covariance_diagnostics.csv`

## Full primary and Monte Carlo outputs

- `DOLAN_PRIMARY_FULL_SIGMA_CURVE.csv`
- `DOLAN_PRIMARY_FULL_SIGMA_CURVE_RAW.json`
- `paired_mc_protocol.json`
- `paired_mc_null_validation.csv`
- `paired_mc_null_validation.json`
- `hertzberg_benchmark_results.csv`

## Full robustness outputs

- `MASTER_ROBUSTNESS_TABLE_V2.csv`
- complete `LOW_SIGMA_Q_SENSITIVITY.csv`
- `LOW_SIGMA_Q_SENSITIVITY_RAW.json`
- complete `HETEROSCEDASTICITY_DECOMPOSITION_RAW.json`
- original `TYPE4_THREE_WAY_AUDIT.csv`
- `SPACING_60_70_80_COLLISION_TYPES.csv`
- complete alternative-spatial-model output table at 97.57841384 MHz
- original physical-gradient scale-up output table
- full LASIQ extracted residual vector
- full LASIQ q-profile table

## Original figures

- `master_robustness_forest_plot_V2.png`
- `low_sigma_q_yield_heatmap.png`
- `low_sigma_q_collision_heatmap.png`
- `heteroscedasticity_decomposition.png`
- `v2_lasiq_falcon_tuning_residual_map.png`
- `v2_lasiq_falcon_q_profile.png`

The `results/figures/` images in this reconstructed repository are newly regenerated summary figures from exact recovered headline values. They are not replacements for the original full-resolution figures above.

## Original implementation files

If available, preserve the original implementations in a tagged archival release before replacing the public clean reference versions:

- `quantum_collision_engine_v2.py`
- `qutech_spatial_model.py`
- `fit_qutech_affine_model.py`
- `paired_mc_protocol.py`
- `run_low_sigma_q_sensitivity.py`
- `run_heteroscedasticity_decomposition.py`

The current `src/` files are transparent public reference implementations, not byte-identical recovery.

## Type-4 one-sided implementation

The exact source implementation used for the historical `hertzberg_fixed_control_one_sided` audit should also be restored from the original V2 collision-engine/audit code if available. Its numerical output is preserved, but this reconstructed repository does not guess the missing operational details.
