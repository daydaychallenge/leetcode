import unittest
from shortest_palindrome import Solution


class TestSolution(unittest.TestCase):
    def test_longestPalindrome_Solution(self):
        sol = Solution()
        self.assertEqual('aaacecaaa', sol.shortestPalindrome('aacecaaa'))
        self.assertEqual('dcbabcd', sol.shortestPalindrome('abcd'))


if __name__ == '__main__':
    unittest.main()
