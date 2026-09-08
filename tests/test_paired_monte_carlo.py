import sys
from pathlib import Path
import unittest
import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from paired_monte_carlo import exact_value_shuffle, paired_summary


class PairedProtocolTests(unittest.TestCase):
    def test_shuffle_preserves_multiset(self):
        rng = np.random.default_rng(1234)
        x = np.array([1.0, 2.0, 3.0, 4.0])
        y = exact_value_shuffle(x, rng)
        self.assertEqual(sorted(x.tolist()), sorted(y.tolist()))

    def test_paired_sign(self):
        out = paired_summary([1, 2, 3], [2, 3, 4])
        self.assertAlmostEqual(out["delta_mean"], -1.0)


if __name__ == "__main__":
    unittest.main()
