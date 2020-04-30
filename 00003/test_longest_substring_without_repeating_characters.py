import unittest
from longest_substring_without_repeating_characters import Solution


class TestSolution(unittest.TestCase):
    def test_Calculate_Solution(self):
        sol = Solution()
        self.assertEqual(1, sol.lengthOfLongestSubstring(' '))
        self.assertEqual(3, sol.lengthOfLongestSubstring('abcabcbb'))
        self.assertEqual(1, sol.lengthOfLongestSubstring('bbbbbb'))
        self.assertEqual(3, sol.lengthOfLongestSubstring('pwwkew'))


if __name__ == '__main__':
    unittest.main()
