import unittest
from groups_of_special_equivalent_strings import Solution


class TestSolution(unittest.TestCase):
    def test_longestPalindrome_Solution(self):
        sol = Solution()
        self.assertEqual(3, sol.numSpecialEquivGroups(["abcd", "cdab", "cbad", "xyzz", "zzxy", "zzyx"]))
        self.assertEqual(3, sol.numSpecialEquivGroups(["abc", "acb", "bac", "bca", "cab", "cba"]))


if __name__ == '__main__':
    unittest.main()
