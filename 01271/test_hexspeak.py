import unittest
from hexspeak import Solution


class TestSolution(unittest.TestCase):
    def test_generateParenthesis_Solution(self):
        sol = Solution()
        self.assertEqual('IOI', sol.toHexspeak('257'))
        self.assertEqual('ERROR', sol.toHexspeak('3'))


if __name__ == '__main__':
    unittest.main()
