import unittest
from generate_parentheses import Solution


class TestSolution(unittest.TestCase):
    def test_generateParenthesis_Solution(self):
        sol = Solution()
        ans = {'()()()', '()(())', '(())()', '(()())', '((()))'}
        self.assertEqual(ans, set(sol.generateParenthesis(3)))
        self.assertEqual(ans, set(sol.generateParenthesis01(3)))


if __name__ == '__main__':
    unittest.main()
