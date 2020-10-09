import unittest
from find_and_replace_pattern import Solution


class TestSolution(unittest.TestCase):
    def test_generateParenthesis_Solution(self):
        sol = Solution()
        self.assertEqual(["mee", "aqq"], sol.findAndReplacePattern(["abc", "deq", "mee", "aqq", "dkd", "ccc"], "abb"))


if __name__ == '__main__':
    unittest.main()
