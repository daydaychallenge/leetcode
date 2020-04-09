import unittest
from rotated_digits import Solution


class TestSolution(unittest.TestCase):
    def test_Calculate_Solution(self):
        sol = Solution()
        self.assertEqual(4, sol.rotatedDigits(10))
        self.assertEqual(15, sol.rotatedDigits(32))
        self.assertEqual(4, sol.rotatedDigits01(10))
        self.assertEqual(15, sol.rotatedDigits01(32))


if __name__ == '__main__':
    unittest.main()
