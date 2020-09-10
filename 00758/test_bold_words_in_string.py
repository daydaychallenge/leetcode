import unittest
from bold_words_in_string import Solution


class TestSolution(unittest.TestCase):
    def test_Calculate_Solution(self):
        sol = Solution()
        self.assertEqual("a<b>abc</b>d", sol.boldWords(["ab", "bc"], "aabcd"))


if __name__ == '__main__':
    unittest.main()
