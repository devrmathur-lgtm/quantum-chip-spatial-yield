from __future__ import annotations
import numpy as np


def collision_free_yield(collision_counts) -> float:
    counts = np.asarray(collision_counts)
    if counts.size == 0:
        raise ValueError("collision_counts must be non-empty")
    return float(np.mean(counts == 0))


def relative_reduction(spatial_mean: float, shuffled_mean: float) -> float:
    if shuffled_mean == 0:
        raise ZeroDivisionError("shuffled mean must be non-zero")
    return (shuffled_mean - spatial_mean) / shuffled_mean


def normal_ci(mean: float, se: float, z: float = 1.959963984540054):
    return mean - z * se, mean + z * se
