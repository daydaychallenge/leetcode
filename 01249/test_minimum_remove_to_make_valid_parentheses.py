import unittest
from minimum_remove_to_make_valid_parentheses import Solution


class TestSolution(unittest.TestCase):
    def test_minRemoveToMakeValid(self):
        sol = Solution()
        self.assertEqual('lee(t(c)o)de', sol.minRemoveToMakeValid('lee(t(c)o)de)'))
        self.assertEqual('ab(c)d', sol.minRemoveToMakeValid('a)b(c)d'))
        self.assertEqual('', sol.minRemoveToMakeValid('))(('))


if __name__ == '__main__':
    unittest.main()
