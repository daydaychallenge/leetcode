import unittest
from interleaving_string import Solution


class TestSolution(unittest.TestCase):
    def test_isValid_Solution(self):
        sol = Solution()
        self.assertTrue(sol.isInterleave("aabcc", "dbbca", "aadbbcbcac"))
        self.assertFalse(sol.isInterleave("aabcc", "dbbca", "aadbbbaccc"))

        self.assertTrue(sol.isInterleaveV01("aabcc", "dbbca", "aadbbcbcac"))
        self.assertFalse(sol.isInterleaveV01("aabcc", "dbbca", "aadbbbaccc"))


if __name__ == '__main__':
    unittest.main()
