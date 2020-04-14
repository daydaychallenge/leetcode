import unittest
from longest_palindromic_substring import Solution


class TestSolution(unittest.TestCase):
    def test_longestPalindrome_Solution(self):
        sol = Solution()
        self.assertEqual('bab', sol.longestPalindrome('babad'))
        self.assertEqual('aaabaaa', sol.longestPalindrome('aaabaaaa'))
        self.assertEqual('bb', sol.longestPalindrome('cbbd'))

        self.assertEqual('bab', sol.longestPalindromeV01('babad'))
        self.assertEqual('aaabaaa', sol.longestPalindromeV01('aaabaaaa'))
        self.assertEqual('bb', sol.longestPalindromeV01('cbbd'))


if __name__ == '__main__':
    unittest.main()
