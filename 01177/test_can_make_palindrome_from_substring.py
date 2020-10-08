import unittest
from can_make_palindrome_from_substring import Solution


class TestSolution(unittest.TestCase):
    def test_generateParenthesis_Solution(self):
        sol = Solution()
        self.assertEqual(
            [True, False, False, True, True],
            sol.canMakePaliQueries("abcda", [[3, 3, 0], [1, 2, 0], [0, 3, 1], [0, 3, 2], [0, 4, 1]])
        )


if __name__ == '__main__':
    unittest.main()
