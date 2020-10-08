import unittest
from smallest_subsequence_of_distinct_characters import Solution


class TestSolution(unittest.TestCase):
    def test_generateParenthesis_Solution(self):
        sol = Solution()
        self.assertEqual("adbc", sol.smallestSubsequence("cdadabcc"))
        self.assertEqual("abcd", sol.smallestSubsequence("abcd"))
        self.assertEqual("eacb", sol.smallestSubsequence("ecbacba"))
        self.assertEqual("letcod", sol.smallestSubsequence("leetcode"))


if __name__ == '__main__':
    unittest.main()
