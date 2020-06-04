import unittest
from distinct_subsequences import Solution


class TestSolution(unittest.TestCase):
    def test_isValid_Solution(self):
        sol = Solution()
        self.assertEqual(3, sol.numDistinct("rabbbit", "rabbit"))
        self.assertEqual(5, sol.numDistinct("babgbag", "bag"))


if __name__ == '__main__':
    unittest.main()
