import unittest
from count_substrings_with_only_one_distinct_letter import Solution


class TestSolution(unittest.TestCase):
    def test_generateParenthesis_Solution(self):
        sol = Solution()
        self.assertEqual(8, sol.countLetters('aaaba'))
        self.assertEqual(55, sol.countLetters('aaaaaaaaaa'))


if __name__ == '__main__':
    unittest.main()
