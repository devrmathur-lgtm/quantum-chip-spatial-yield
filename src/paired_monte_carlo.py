"""Helpers for the paired exact-value shuffle control.

Reconstructed public implementation based on the final frozen protocol.
"""

from __future__ import annotations
import numpy as np


def exact_value_shuffle(errors, rng: np.random.Generator):
    """Return a permutation of the exact same realized values."""
    arr = np.asarray(errors, dtype=float)
    return arr[rng.permutation(arr.size)]


def paired_effect(spatial_metric, shuffled_metric):
    """Spatial minus shuffled, matching the project's sign convention."""
    return np.asarray(spatial_metric) - np.asarray(shuffled_metric)


def paired_summary(spatial_metric, shuffled_metric):
    spatial = np.asarray(spatial_metric, dtype=float)
    shuffled = np.asarray(shuffled_metric, dtype=float)
    if spatial.shape != shuffled.shape:
        raise ValueError("paired arrays must have identical shapes")
    delta = paired_effect(spatial, shuffled)
    return {
        "n": int(delta.size),
        "spatial_mean": float(spatial.mean()),
        "shuffled_mean": float(shuffled.mean()),
        "delta_mean": float(delta.mean()),
        "delta_se": float(delta.std(ddof=1) / np.sqrt(delta.size)) if delta.size > 1 else 0.0,
    }
