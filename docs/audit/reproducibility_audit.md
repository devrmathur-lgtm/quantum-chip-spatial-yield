# Reproducibility audit

The final V2 project audit recorded:

- 24/24 final reproducibility checks passed
- 20/20 frozen hashes unchanged

The audited checks covered, among other items:

- collision-engine unit checks
- heavy-hex graph counts
- collision-type sum consistency
- deterministic seed behavior
- covariance positive-definiteness
- IID exchangeability controls
- frozen primary result
- low-sigma q analyses
- heteroscedasticity decomposition
- Type-4 audit

## Current reconstructed repository limitation

The original V2 hash manifest and the byte-identical original generated files are not retrievable in the current file store.

For that reason, this reconstructed package does not claim that its newly generated files reproduce the historical SHA-256 values.

The old frozen-state statement is preserved as an audit fact, while the new repository has its own `docs/audit/repository_manifest.sha256`.
