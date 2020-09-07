import unittest
from rearrange_words_in_a_sentence import Solution


class TestSolution(unittest.TestCase):
    def test_Calculate_Solution(self):
        sol = Solution()
        self.assertEqual("Is cool leetcode", sol.arrangeWords("Leetcode is cool"))
        self.assertEqual("On and keep calm code", sol.arrangeWords("Keep calm and code on"))


if __name__ == '__main__':
    unittest.main()
