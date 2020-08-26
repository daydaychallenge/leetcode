import unittest
from basic_calculator_iii import Solution


class TestSolution(unittest.TestCase):
    def test_isValid_Solution(self):
        sol = Solution()
        self.assertEqual(2, sol.calculate("1 + 1"))
        self.assertEqual(4, sol.calculate(" 6-4 / 2 "))
        self.assertEqual(21, sol.calculate("2*(5+5*2)/3+(6/2+8)"))
        self.assertEqual(-12, sol.calculate("(2+6* 3+5- (3*14/7+2)*5)+3"))


if __name__ == '__main__':
    unittest.main()
