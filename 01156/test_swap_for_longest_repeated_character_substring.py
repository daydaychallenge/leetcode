import unittest
from swap_for_longest_repeated_character_substring import Solution


class TestSolution(unittest.TestCase):
    def test_generateParenthesis_Solution(self):
        sol = Solution()
        self.assertEqual(3, sol.maxRepOpt1("ababa"))
        self.assertEqual(6, sol.maxRepOpt1("aaabaaa"))
        self.assertEqual(4, sol.maxRepOpt1("aaabbaaa"))
        self.assertEqual(5, sol.maxRepOpt1("aaaaa"))


if __name__ == '__main__':
    unittest.main()
