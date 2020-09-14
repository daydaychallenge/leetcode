import unittest
from last_substring_in_lexicographical_order import Solution


class TestSolution(unittest.TestCase):
    def test_minRemoveToMakeValid(self):
        sol = Solution()
        self.assertEqual("bab", sol.lastSubstring("abab"))
        self.assertEqual("tcode", sol.lastSubstring("leetcode"))


if __name__ == '__main__':
    unittest.main()
