import unittest
from find_the_closest_palindrome import Solution


class TestSolution(unittest.TestCase):
    def test_isValid_Solution(self):
        sol = Solution()
        self.assertEqual("121", sol.nearestPalindromic("123"))


if __name__ == '__main__':
    unittest.main()
