import unittest
from reverse_words_in_a_string_ii import Solution


class TestSolution(unittest.TestCase):
    def test_longestPalindrome_Solution(self):
        sol = Solution()
        s = ['t', 'h', 'e', ' ', 's', 'k', 'y', ' ', 'i', 's', ' ', 'b', 'l', 'u', 'e']
        r = ['b', 'l', 'u', 'e', ' ', 'i', 's', ' ', 's', 'k', 'y', ' ', 't', 'h', 'e']

        sol.reverseWords(s)
        self.assertEqual(r, s)


if __name__ == '__main__':
    unittest.main()
