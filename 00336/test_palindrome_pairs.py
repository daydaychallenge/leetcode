import unittest
from palindrome_pairs import Solution


class TestSolution(unittest.TestCase):
    def test_longestPalindrome_Solution(self):
        sol = Solution()
        self.assertEqual([[0, 1], [1, 0], [3, 2], [2, 4]], sol.palindromePairs(['abcd', 'dcba', 'lls', 's', 'sssll']))
        self.assertEqual([[0, 1], [1, 0]], sol.palindromePairs(['bat', 'tab', 'cat']))


if __name__ == '__main__':
    unittest.main()
