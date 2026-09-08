"""Recovered spatial-model constants and validation helpers.

The original full covariance matrix is not reconstructed here.
"""

from __future__ import annotations
import numpy as np

PRIMARY_SIGMA_F_MHZ = 97.57841384
PRIMARY_Q = 0.67549
Q_LOWER_BOUND = 0.4852

PLANAR17_PITCH_X_MM = 2.315
PLANAR17_PITCH_Y_MM = 2.301

PROCESSOR_QUBITS = 65
PROCESSOR_EDGES = 72

NOMINAL_FREQUENCIES_GHZ = (5.00, 5.07, 5.14)


def is_symmetric(matrix, atol=1e-10):
    m = np.asarray(matrix, dtype=float)
    return m.ndim == 2 and m.shape[0] == m.shape[1] and np.allclose(m, m.T, atol=atol)


def min_eigenvalue(matrix):
    m = np.asarray(matrix, dtype=float)
    if not is_symmetric(m):
        raise ValueError("covariance matrix must be square and symmetric")
    return float(np.linalg.eigvalsh(m).min())


def is_positive_semidefinite(matrix, tol=1e-10):
    return min_eigenvalue(matrix) >= -tol
