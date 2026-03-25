import unittest
import numpy as np

from week_1.engineering.task_08 import simulate_multiple_walks_clumsy


class TestEndSteps(unittest.TestCase):

    def test_final_positions_range(self):
        all_walks = simulate_multiple_walks_clumsy(n_walks=500, seed=123)
        final_positions = all_walks[:, -1]
        self.assertTrue(np.all(final_positions >= 0))

    def test_ends_length(self):
        all_walks = simulate_multiple_walks_clumsy(n_walks=500, seed=123)
        self.assertEqual(all_walks.shape, (500, 101))

if __name__ == "__main__":
    unittest.main()