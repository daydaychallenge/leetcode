import unittest
from count_different_palindromic_subsequences import Solution


class TestSolution(unittest.TestCase):
    def test_isValid_Solution(self):
        sol = Solution()
        self.assertEqual(6, sol.countPalindromicSubsequences('bccb'))
        self.assertEqual(104860361, sol.countPalindromicSubsequences(
            'abcdabcdabcdabcdabcdabcdabcdabcddcbadcbadcbadcbadcbadcbadcbadcba'
        ))


if __name__ == '__main__':
    unittest.main()
