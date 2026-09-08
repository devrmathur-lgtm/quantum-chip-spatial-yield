"""Public reference collision predicates for the reconstructed repository.

This file is reconstructed from the final frozen project specification.
It is not claimed to be byte-identical to the archived working script.
"""

from __future__ import annotations
from dataclasses import dataclass
from typing import Iterable

ALPHA_MHZ = -330.0

TOLERANCE_MHZ = {
    1: 17.0,
    2: 4.0,
    3: 30.0,
    5: 17.0,
    6: 25.0,
    7: 17.0,
}


def f12(f01: float, alpha: float = ALPHA_MHZ) -> float:
    return f01 + alpha


def f02(f01: float, alpha: float = ALPHA_MHZ) -> float:
    return 2.0 * f01 + alpha


def within(value: float, target: float, tolerance: float) -> bool:
    return abs(value - target) < tolerance


def type1(fj: float, fk: float) -> bool:
    """Nearest-neighbor 01/01 collision."""
    return within(fj, fk, TOLERANCE_MHZ[1])


def type2(fj_control: float, fk_target: float, alpha: float = ALPHA_MHZ) -> bool:
    """Two-photon 02 control transition near twice the target 01 frequency."""
    return within(f02(fj_control, alpha), 2.0 * fk_target, TOLERANCE_MHZ[2])


def type3(fj: float, fk: float, alpha: float = ALPHA_MHZ) -> bool:
    """01 transition of one qubit near the 12 transition of the other."""
    return (
        within(fj, f12(fk, alpha), TOLERANCE_MHZ[3])
        or within(fk, f12(fj, alpha), TOLERANCE_MHZ[3])
    )


def type4_symmetric(fc: float, ft: float, alpha: float = ALPHA_MHZ) -> bool:
    """Frozen later IBM/LASIQ symmetric Type-4 failure convention.

    With alpha < 0, the desired cross-resonance control-target separation
    is treated as lying within one anharmonicity magnitude.
    """
    return abs(fc - ft) > abs(alpha)


def type4_hertzberg_table_condition(
    fc: float, ft: float, alpha: float = ALPHA_MHZ
) -> bool:
    """Recovered literal Hertzberg Table-I directional condition.

    This is the condition visible in the published table:
        f_target,01 < f_control,12 OR f_control,01 < f_target,01

    The project's separate fixed-control one-sided audit mode used additional
    operational conventions that are not fully recoverable from the current
    archived record, so it is intentionally not reimplemented here.
    """
    return (ft < f12(fc, alpha)) or (fc < ft)


def type5(fj: float, fi: float) -> bool:
    return within(fj, fi, TOLERANCE_MHZ[5])


def type6(fi: float, fk: float, alpha: float = ALPHA_MHZ) -> bool:
    return (
        within(fi, f12(fk, alpha), TOLERANCE_MHZ[6])
        or within(f12(fi, alpha), fk, TOLERANCE_MHZ[6])
    )


def type7(fj: float, fk: float, fi: float, alpha: float = ALPHA_MHZ) -> bool:
    return within(f02(fj, alpha), fk + fi, TOLERANCE_MHZ[7])


@dataclass(frozen=True)
class CollisionCounts:
    type1: int = 0
    type2: int = 0
    type3: int = 0
    type4: int = 0
    type5: int = 0
    type6: int = 0
    type7: int = 0

    @property
    def total(self) -> int:
        return sum(
            (
                self.type1, self.type2, self.type3, self.type4,
                self.type5, self.type6, self.type7
            )
        )
