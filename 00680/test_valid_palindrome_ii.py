import unittest
from valid_palindrome_ii import Solution


class TestSolution(unittest.TestCase):
    def test_valid_palindrome(self):
        sol = Solution()
        self.assertTrue(sol.validPalindrome('aba'))
        self.assertTrue(sol.validPalindrome('abca'))


if __name__ == '__main__':
    unittest.main()
