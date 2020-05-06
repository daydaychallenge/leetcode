import unittest
from subarrays_with_k_different_integers import Solution


class TestSolution(unittest.TestCase):
    def test_Calculate_Solution(self):
        sol = Solution()
        self.assertEqual(7, sol.subarraysWithKDistinct([1, 2, 1, 2, 3], 2))
        self.assertEqual(3, sol.subarraysWithKDistinct([1, 2, 1, 3, 4], 3))


if __name__ == '__main__':
    unittest.main()
