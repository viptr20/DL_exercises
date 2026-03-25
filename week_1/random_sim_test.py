import unittest
import numpy as np

from random_sim import simulate_once


class TestSimulateOnce(unittest.TestCase):
    def test_when_called_with_seed_then_returns_values_in_expected_ranges(self):
        rand_float, d1, d2, dice, step = simulate_once(seed=123)

        self.assertIsInstance(rand_float, float)
        self.assertIsInstance(d1, int)
        self.assertIsInstance(d2, int)
        self.assertIsInstance(dice, int)
        self.assertIsInstance(step, int)

        self.assertTrue(0.0 <= rand_float < 1.0)
        self.assertIn(d1, range(1, 7))
        self.assertIn(d2, range(1, 7))
        self.assertIn(dice, range(1, 7))
        self.assertTrue(step > 0)

    def test_when_called_with_fixed_seed_then_returns_deterministic_values(self):
        result1 = simulate_once(seed=123)
        result2 = simulate_once(seed=123)
        self.assertEqual(result1, result2)

    def test_when_called_with_different_seeds_then_results_may_differ(self):
        result1 = simulate_once(seed=123)
        result2 = simulate_once(seed=456)
        self.assertNotEqual(result1, result2)


if __name__ == "__main__":
    unittest.main()
