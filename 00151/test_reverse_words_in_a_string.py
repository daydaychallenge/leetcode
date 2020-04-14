import unittest
from reverse_words_in_a_string import Solution


class TestSolution(unittest.TestCase):
    def test_longestPalindrome_Solution(self):
        sol = Solution()
        self.assertEqual('world! hello', sol.reverseWords('  hello world!  '))
        self.assertEqual('example good a', sol.reverseWords('a good   example'))

        self.assertEqual('world! hello', sol.reverseWordsV01('  hello world!  '))
        self.assertEqual('example good a', sol.reverseWordsV01('a good   example'))


if __name__ == '__main__':
    unittest.main()
