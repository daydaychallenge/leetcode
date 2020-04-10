import unittest
from valid_parentheses import Solution


class TestSolution(unittest.TestCase):
    def test_isValid_Solution(self):
        sol = Solution()
        self.assertTrue(sol.isValid('()[]{}'))
        self.assertFalse(sol.isValid('{(['))
        self.assertFalse(sol.isValid(']})'))
        self.assertFalse(sol.isValid('[(])'))
        self.assertFalse(sol.isValid('((}}'))


if __name__ == '__main__':
    unittest.main()
