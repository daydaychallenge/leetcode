import unittest
from find_the_longest_substring_containing_vowels_in_even_counts import Solution


class TestSolution(unittest.TestCase):
    def test_Calculate_Solution(self):
        sol = Solution()
        self.assertEqual(13, sol.findTheLongestSubstring('eleetminicoworoep'))
        self.assertEqual(5, sol.findTheLongestSubstring('leetcodeisgreat'))
        self.assertEqual(6, sol.findTheLongestSubstring('bcbcbc'))


if __name__ == '__main__':
    unittest.main()
