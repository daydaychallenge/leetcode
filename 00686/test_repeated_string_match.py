import unittest
from repeated_string_match import Solution


class TestSolution(unittest.TestCase):
    def test_generateParenthesis_Solution(self):
        sol = Solution()
        self.assertEqual(3, sol.repeatedStringMatch("abcd", "cdabcdab"))
        self.assertEqual(2, sol.repeatedStringMatch("a", "aa"))
        self.assertEqual(1, sol.repeatedStringMatch("a", "a"))
        self.assertEqual(-1, sol.repeatedStringMatch("abc", "wxyz"))


if __name__ == '__main__':
    unittest.main()
