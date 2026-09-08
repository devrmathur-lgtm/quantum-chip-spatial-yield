import sys
from pathlib import Path
import unittest
import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

import spatial_model as sm


class SpatialModelTests(unittest.TestCase):
    def test_recovered_constants(self):
        self.assertAlmostEqual(sm.PRIMARY_SIGMA_F_MHZ, 97.57841384)
        self.assertAlmostEqual(sm.PRIMARY_Q, 0.67549)
        self.assertEqual(sm.PROCESSOR_QUBITS, 65)
        self.assertEqual(sm.PROCESSOR_EDGES, 72)

    def test_psd_helper(self):
        self.assertTrue(sm.is_positive_semidefinite(np.eye(3)))


if __name__ == "__main__":
    unittest.main()
