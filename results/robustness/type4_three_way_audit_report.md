# Three-way Type-4 audit

Three plausible Type-4 conventions were compared:

1. `lasiq_symmetric`
2. `hertzberg_fixed_control_one_sided`
3. `hertzberg_literal`

## External high-spread benchmark

At sigma_f = 132.3 MHz and 70 MHz nominal spacing:

- symmetric: 24.7809 collisions
- one-sided: 24.0014
- literal: 44.3393

The literature benchmark is approximately 25 collisions, so both symmetric and one-sided rules are benchmark-compatible.

A spacing scan gave closest values of approximately:

- symmetric: 25.044 at 72 MHz
- one-sided: 25.055 at 78 MHz
- literal: 43.760 at its closest tested spacing

## Primary spatial effect

At 97.57841384 MHz:

- symmetric: 14.1001 spatial, 19.1225 shuffled, delta -5.0224
- literal: 22.3292 spatial, 33.9147 shuffled, delta -11.5855
- one-sided: delta -4.7843, 95% CI [-4.8176, -4.7510]

The sign of the spatial effect is robust to all three tested interpretations.

The final project retained the symmetric later IBM/LASIQ convention for production, while explicitly acknowledging that the external benchmark does not uniquely resolve the historical Type-4 implementation.

## Reference-code recovery boundary

The numerical result for the fixed-control one-sided mode is preserved in the CSV above. The exact original implementation details for that separate audit mode are not sufficiently represented in the surviving project record to recreate the code without guessing.

For that reason, `src/collision_engine.py` implements the frozen production symmetric convention and the literal published Table-I condition only.
