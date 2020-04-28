import unittest
from sum_of_two_integers import Solution


class TestSolution(unittest.TestCase):
    def test_longestPalindrome_Solution(self):
        sol = Solution()
        self.assertEqual(3, sol.getSum(1, 2))
        self.assertEqual(1, sol.getSum(-2, 3))
        self.assertEqual(-3, sol.getSum(-6, 3))


if __name__ == '__main__':
    unittest.main()
