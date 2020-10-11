import unittest
from word_subsets import Solution


class TestSolution(unittest.TestCase):
    def test_generateParenthesis_Solution(self):
        sol = Solution()
        self.assertEqual(
            {"facebook", "google", "leetcode"},
            set(sol.wordSubsets(["amazon", "apple", "facebook", "google", "leetcode"], ["e", "o"]))
        )
        self.assertEqual(
            {"apple", "google", "leetcode"},
            set(sol.wordSubsets(["amazon", "apple", "facebook", "google", "leetcode"], ["l", "e"]))
        )
        self.assertEqual(
            {"facebook", "google"},
            set(sol.wordSubsets(["amazon", "apple", "facebook", "google", "leetcode"], ["oo", "e"]))
        )


if __name__ == '__main__':
    unittest.main()
