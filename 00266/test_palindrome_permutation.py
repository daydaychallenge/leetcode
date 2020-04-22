import unittest
from palindrome_permutation import Solution


class TestSolution(unittest.TestCase):
    def test_Calculate_Solution(self):
        sol = Solution()

        self.assertTrue(sol.canPermutePalindrome('aab'))
        self.assertFalse(sol.canPermutePalindrome('code'))


if __name__ == '__main__':
    unittest.main()
