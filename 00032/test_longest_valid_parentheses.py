import unittest
from longest_valid_parentheses import Solution


class TestSolution(unittest.TestCase):
    def test_generateParenthesis_Solution(self):
        sol = Solution()
        self.assertEqual(2, sol.longestValidParentheses('(()'))
        self.assertEqual(4, sol.longestValidParentheses(')()())'))


if __name__ == '__main__':
    unittest.main()
