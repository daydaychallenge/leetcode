import unittest
from replace_the_substring_for_balanced_string import Solution


class TestSolution(unittest.TestCase):
    def test_generateParenthesis_Solution(self):
        sol = Solution()
        self.assertEqual(0, sol.balancedString("QWER"))
        self.assertEqual(2, sol.balancedString("QQQW"))
        self.assertEqual(3, sol.balancedString("QQQQ"))


if __name__ == '__main__':
    unittest.main()
