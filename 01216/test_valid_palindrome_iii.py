import unittest
from valid_palindrome_iii import Solution


class TestSolution(unittest.TestCase):
    def test_generateParenthesis_Solution(self):
        sol = Solution()
        self.assertTrue(sol.isValidPalindrome('abcdeca', 2))


if __name__ == '__main__':
    unittest.main()
