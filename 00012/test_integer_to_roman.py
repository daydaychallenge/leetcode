import unittest
from integer_to_roman import Solution


class TestSolution(unittest.TestCase):
    def test_Calculate_Solution(self):
        sol = Solution()
        self.assertEqual('III', sol.intToRoman(3))
        self.assertEqual('IV', sol.intToRoman(4))
        self.assertEqual('IX', sol.intToRoman(9))
        self.assertEqual('LVIII', sol.intToRoman(58))
        self.assertEqual('MCMXCIV', sol.intToRoman(1994))


if __name__ == '__main__':
    unittest.main()
