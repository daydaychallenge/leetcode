import unittest
from greatest_common_divisor_of_strings import Solution


class TestSolution(unittest.TestCase):
    def test_generateParenthesis_Solution(self):
        sol = Solution()
        self.assertEqual('ABC', sol.gcdOfStrings('ABCABC', 'ABC'))
        self.assertEqual('AB', sol.gcdOfStrings('ABAB', 'ABABAB'))
        self.assertEqual('', sol.gcdOfStrings('ABC', 'AB'))


if __name__ == '__main__':
    unittest.main()
