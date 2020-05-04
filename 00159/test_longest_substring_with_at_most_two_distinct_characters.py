import unittest
from longest_substring_with_at_most_two_distinct_characters import Solution


class TestSolution(unittest.TestCase):
    def test_Calculate_Solution(self):
        sol = Solution()
        self.assertEqual(3, sol.lengthOfLongestSubstringTwoDistinct('eceba'))
        self.assertEqual(5, sol.lengthOfLongestSubstringTwoDistinct('ccaabbb'))


if __name__ == '__main__':
    unittest.main()
