import unittest
from basic_calculator_iv import Solution


class TestSolution(unittest.TestCase):
    def test_isValid_Solution(self):
        sol = Solution()
        self.assertEqual(["-1*a", "14"], sol.basicCalculatorIV("e + 8 - a + 5", ["e"], [1]))
        self.assertEqual(["-1*pressure", "5"], sol.basicCalculatorIV(
            "e - 8 + temperature - pressure", ["e", "temperature"], [1, 12]
        ))
        self.assertEqual(["1*e*e","-64"], sol.basicCalculatorIV("(e + 8) * (e - 8)", [], []))
        self.assertEqual([], sol.basicCalculatorIV("7 - 7", [], []))
        self.assertEqual(["5*a*b*c"], sol.basicCalculatorIV("a * b * c + b * a * c * 4", [], []))
        self.assertEqual([
            "-1*a*a*b*b", "2*a*a*b*c", "-1*a*a*c*c", "1*a*b*b*b", "-1*a*b*b*c", "-1*a*b*c*c",
            "1*a*c*c*c", "-1*b*b*b*c", "2*b*b*c*c", "-1*b*c*c*c", "2*a*a*b", "-2*a*a*c", "-2*a*b*b",
            "2*a*c*c", "1*b*b*b", "-1*b*b*c", "1*b*c*c", "-1*c*c*c", "-1*a*a", "1*a*b", "1*a*c", "-1*b*c"],
            sol.basicCalculatorIV(
                "((a - b) * (b - c) + (c - a)) * ((a - b) + (b - c) * (c - a))",
                [], []
            ))


if __name__ == '__main__':
    unittest.main()
