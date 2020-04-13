import unittest
from zigzag_conversion import Solution


class TestSolution(unittest.TestCase):
    def test_isValid_Solution(self):
        sol = Solution()
        self.assertEqual('PAHNAPLSIIGYIR', sol.convert('PAYPALISHIRING', 3))
        self.assertEqual('PINALSIGYAHRPI', sol.convert('PAYPALISHIRING', 4))


if __name__ == '__main__':
    unittest.main()
