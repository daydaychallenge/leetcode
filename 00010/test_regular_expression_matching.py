import unittest
from regular_expression_matching import Solution


class TestSolution(unittest.TestCase):
    def test_longestPalindrome_Solution(self):
        sol = Solution()
        self.assertFalse(sol.isMatch("aa", "a"))
        self.assertTrue(sol.isMatch("aa", "a*"))
        self.assertTrue(sol.isMatch("ab", ".*"))
        self.assertTrue(sol.isMatch("aab", "c*a*b"))
        self.assertFalse(sol.isMatch("mississippi", "mis*is*p*."))

        self.assertFalse(sol.isMatchV01("aa", "a"))
        self.assertTrue(sol.isMatchV01("aa", "a*"))
        self.assertTrue(sol.isMatchV01("ab", ".*"))
        self.assertTrue(sol.isMatchV01("aab", "c*a*b"))
        self.assertFalse(sol.isMatchV01("mississippi", "mis*is*p*."))


if __name__ == '__main__':
    unittest.main()
