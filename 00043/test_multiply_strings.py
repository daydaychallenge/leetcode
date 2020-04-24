import unittest
from multiply_strings import Solution


class TestSolution(unittest.TestCase):
    def test_longestPalindrome_Solution(self):
        sol = Solution()
        self.assertEqual('6', sol.multiply('2', '3'))
        self.assertEqual('56088', sol.multiply('123', '456'))


if __name__ == '__main__':
    unittest.main()
