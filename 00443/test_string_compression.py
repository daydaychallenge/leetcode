import unittest
from string_compression import Solution


class TestSolution(unittest.TestCase):
    def test_longestPalindrome_Solution(self):
        sol = Solution()
        chars = ['a', 'a', 'b', 'b', 'c', 'c', 'c', 'd']
        self.assertEqual(7, sol.compress(chars))
        self.assertEqual(['a', '2', 'b', '2', 'c', '3', 'd'], chars[:7])


if __name__ == '__main__':
    unittest.main()
