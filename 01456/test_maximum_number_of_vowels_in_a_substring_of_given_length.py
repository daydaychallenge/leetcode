import unittest
from maximum_number_of_vowels_in_a_substring_of_given_length import Solution


class TestSolution(unittest.TestCase):
    def test_generateParenthesis_Solution(self):
        sol = Solution()
        self.assertEqual(3, sol.maxVowels("abciiidef", 3))
        self.assertEqual(2, sol.maxVowels("leetcode", 3))
        self.assertEqual(0, sol.maxVowels("rhythms", 4))


if __name__ == '__main__':
    unittest.main()
