import unittest
from decode_ways import Solution


class TestSolution(unittest.TestCase):
    def test_isValid_Solution(self):
        sol = Solution()
        self.assertEqual(2, sol.numDecodings("12"))
        self.assertEqual(3, sol.numDecodings("226"))
        self.assertEqual(1, sol.numDecodings("10"))
        self.assertEqual(1, sol.numDecodings("1"))


if __name__ == '__main__':
    unittest.main()
