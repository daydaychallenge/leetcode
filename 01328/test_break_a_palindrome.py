import unittest
from break_a_palindrome import Solution


class TestSolution(unittest.TestCase):
    def test_minRemoveToMakeValid(self):
        sol = Solution()
        self.assertEqual("aaccba", sol.breakPalindrome("abccba"))
        self.assertEqual("", sol.breakPalindrome("a"))
        self.assertEqual("ab", sol.breakPalindrome("aa"))

        self.assertEqual("aaccba", sol.breakPalindrome01("abccba"))
        self.assertEqual("", sol.breakPalindrome01("a"))
        self.assertEqual("ab", sol.breakPalindrome01("aa"))


if __name__ == '__main__':
    unittest.main()
