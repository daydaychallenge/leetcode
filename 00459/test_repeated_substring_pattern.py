import unittest
from repeated_substring_pattern import Solution


class TestSolution(unittest.TestCase):
    def test_generateParenthesis_Solution(self):
        sol = Solution()
        self.assertTrue(sol.repeatedSubstringPattern("abab"))
        self.assertTrue(sol.repeatedSubstringPattern("abcabcabcabc"))
        self.assertFalse(sol.repeatedSubstringPattern("aba"))


if __name__ == '__main__':
    unittest.main()
