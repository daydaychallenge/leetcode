import unittest
from maximum_number_of_occurrences_of_a_substring import Solution


class TestSolution(unittest.TestCase):
    def test_generateParenthesis_Solution(self):
        sol = Solution()
        self.assertEqual(2, sol.maxFreq("aababcaab", 2, 3, 4))
        self.assertEqual(2, sol.maxFreq("aaaa", 1, 3, 3))
        self.assertEqual(3, sol.maxFreq("aabcabcab", 2, 2, 3))
        self.assertEqual(0, sol.maxFreq("abcde", 2, 3, 3))


if __name__ == '__main__':
    unittest.main()
