import unittest
from basic_calculator_ii import Solution


class TestSolution(unittest.TestCase):
    def test_isValid_Solution(self):
        sol = Solution()
        self.assertEqual(7, sol.calculate("3+2*2"))
        self.assertEqual(1, sol.calculate(" 3/2 "))
        self.assertEqual(1, sol.calculate(" 3-5 / 2 "))


if __name__ == '__main__':
    unittest.main()
