import unittest
from reverse_vowels_of_a_string import Solution


class TestSolution(unittest.TestCase):
    def test_isValid_Solution(self):
        sol = Solution()
        self.assertEqual("holle", sol.reverseVowels("hello"))
        self.assertEqual("leotcede", sol.reverseVowels("leetcode"))


if __name__ == '__main__':
    unittest.main()
