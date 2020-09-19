import unittest
from valid_parenthesis_string import Solution


class TestSolution(unittest.TestCase):
    def test_minRemoveToMakeValid(self):
        sol = Solution()
        self.assertTrue(sol.checkValidString('(*)'))
        self.assertTrue(sol.checkValidString('((*)'))
        self.assertTrue(sol.checkValidString('(*()'))
        self.assertFalse(sol.checkValidString('())(*'))


if __name__ == '__main__':
    unittest.main()
