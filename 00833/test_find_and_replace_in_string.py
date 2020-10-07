import unittest
from find_and_replace_in_string import Solution


class TestSolution(unittest.TestCase):
    def test_generateParenthesis_Solution(self):
        sol = Solution()
        self.assertEqual("eeebffff", sol.findReplaceString("abcd", [0, 2], ["a", "cd"], ["eee", "ffff"]))
        self.assertEqual("eeecd", sol.findReplaceString("abcd", [0, 2], ["ab", "ec"], ["eee", "ffff"]))


if __name__ == '__main__':
    unittest.main()
