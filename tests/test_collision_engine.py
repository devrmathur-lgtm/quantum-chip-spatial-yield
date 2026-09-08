import sys
from pathlib import Path
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

import collision_engine as ce


class CollisionPredicateTests(unittest.TestCase):
    def test_transition_definitions(self):
        self.assertEqual(ce.f12(5000.0), 4670.0)
        self.assertEqual(ce.f02(5000.0), 9670.0)

    def test_type1_window(self):
        self.assertTrue(ce.type1(5000.0, 5016.0))
        self.assertFalse(ce.type1(5000.0, 5017.0))

    def test_type3_symmetric(self):
        self.assertTrue(ce.type3(5000.0, 5330.0))

    def test_type4_symmetric_boundary(self):
        self.assertFalse(ce.type4_symmetric(5000.0, 5330.0))
        self.assertTrue(ce.type4_symmetric(5000.0, 5331.0))


if __name__ == "__main__":
    unittest.main()
