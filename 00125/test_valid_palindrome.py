import unittest
from valid_palindrome import Solution


class TestSolution(unittest.TestCase):
    def test_isValid_Solution(self):
        sol = Solution()
        self.assertTrue(sol.isPalindrome("A man, a plan, a canal: Panama"))
        self.assertFalse(sol.isPalindrome("race a car"))


if __name__ == '__main__':
    unittest.main()
