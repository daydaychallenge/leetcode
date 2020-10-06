import unittest
from string_compression_ii import Solution


class TestSolution(unittest.TestCase):
    def test_generateParenthesis_Solution(self):
        sol = Solution()
        self.assertEqual(4, sol.getLengthOfOptimalCompression("aaabcccd", 2))
        self.assertEqual(2, sol.getLengthOfOptimalCompression("aabbaa", 2))
        self.assertEqual(5, sol.getLengthOfOptimalCompression("xyzaabbbaa", 3))


if __name__ == '__main__':
    unittest.main()
