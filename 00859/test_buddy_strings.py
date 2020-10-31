import unittest
from buddy_strings import Solution


class TestSolution(unittest.TestCase):
    def test_generateParenthesis_Solution(self):
        sol = Solution()
        self.assertTrue(sol.buddyStrings("ab", "ba"))
        self.assertFalse(sol.buddyStrings("ab", "ab"))
        self.assertTrue(sol.buddyStrings("aa", "aa"))
        self.assertTrue(sol.buddyStrings("aaaaaaabc", "aaaaaaacb"))
        

if __name__ == '__main__':
    unittest.main()
