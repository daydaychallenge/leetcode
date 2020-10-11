import unittest
from increasing_decreasing_string import Solution


class TestSolution(unittest.TestCase):
    def test_generateParenthesis_Solution(self):
        sol = Solution()
        self.assertEqual("abccbaabccba", sol.sortString("aaaabbbbcccc"))
        self.assertEqual("art", sol.sortString("rat"))
        self.assertEqual("cdelotee", sol.sortString("leetcode"))
        self.assertEqual("ops", sol.sortString("spo"))


if __name__ == '__main__':
    unittest.main()
