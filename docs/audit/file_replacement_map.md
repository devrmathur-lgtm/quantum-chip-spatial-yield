# Historical file replacement map

The public repository removes internal revision labels such as `V2`, `FINAL`, and `STEP6`.

Use `github_file_map.csv` for the exact mapping.

General rules:

- final V2 reports become clean descriptive names under `docs/`
- `quantum_collision_engine_v2.py` becomes `src/collision_engine.py`
- frozen protocols remain conceptually frozen but receive clean public paths
- STEP6 and older V1 reports are excluded
- work-bundle ZIP files are excluded
- original binary data artifacts are retained by historical filename only when they are restored, because renaming third-party-derived data can obscure provenance
