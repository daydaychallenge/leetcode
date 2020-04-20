import unittest
from palindromic_substrings import Solution


class TestSolution(unittest.TestCase):
    def test_longestPalindrome_Solution(self):
        sol = Solution()
        self.assertEqual(3, sol.countSubstrings('abc'))
        self.assertEqual(6, sol.countSubstrings('aaa'))


if __name__ == '__main__':
    unittest.main()
