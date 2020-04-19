import unittest
from longest_palindromic_subsequence import Solution


class TestSolution(unittest.TestCase):
    def test_longestPalindrome_Solution(self):
        sol = Solution()
        self.assertEqual(4, sol.longestPalindromeSubseq('bbbab'))
        self.assertEqual(2, sol.longestPalindromeSubseq('cbbd'))


if __name__ == '__main__':
    unittest.main()
