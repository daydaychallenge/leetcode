import unittest
from longest_uncommon_subsequence_ii import Solution


class TestSolution(unittest.TestCase):
    def test_generateParenthesis_Solution(self):
        sol = Solution()
        self.assertEqual(3, sol.findLUSlength(["aba", "cdc", "eae"]))


if __name__ == '__main__':
    unittest.main()
