import unittest
from valid_word_abbreviation import Solution


class TestSolution(unittest.TestCase):
    def test_generateParenthesis_Solution(self):
        sol = Solution()
        self.assertTrue(sol.validWordAbbreviation("internationalization", "i12iz4n"))
        self.assertFalse(sol.validWordAbbreviation("apple", "a2e"))


if __name__ == '__main__':
    unittest.main()
