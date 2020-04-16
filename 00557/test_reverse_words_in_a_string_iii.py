import unittest
from reverse_words_in_a_string_iii import Solution


class TestSolution(unittest.TestCase):
    def test_isValid_Solution(self):
        sol = Solution()
        self.assertEqual("s'teL ekat edoCteeL tsetnoc", sol.reverseWords("Let's take LeetCode contest"))


if __name__ == '__main__':
    unittest.main()
