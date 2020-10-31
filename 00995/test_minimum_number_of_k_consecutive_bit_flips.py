import unittest
from minimum_number_of_k_consecutive_bit_flips import Solution


class TestSolution(unittest.TestCase):
    def test_generateParenthesis_Solution(self):
        sol = Solution()
        self.assertEqual(2, sol.minKBitFlips([0, 1, 0], 1))
        self.assertEqual(-1, sol.minKBitFlips([1, 1, 0], 2))
        self.assertEqual(3, sol.minKBitFlips([0, 0, 0, 1, 0, 1, 1, 0], 3))


if __name__ == '__main__':
    unittest.main()
