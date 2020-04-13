import unittest
from roman_to_integer import Solution


class TestSolution(unittest.TestCase):
    def test_isValid_Solution(self):
        sol = Solution()
        self.assertEqual(58, sol.romanToInt('LVIII'))
        self.assertEqual(1994, sol.romanToInt('MCMXCIV'))


if __name__ == '__main__':
    unittest.main()
