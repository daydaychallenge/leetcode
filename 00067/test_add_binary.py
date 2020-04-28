import unittest
from add_binary import Solution


class TestSolution(unittest.TestCase):
    def test_longestPalindrome_Solution(self):
        sol = Solution()
        self.assertEqual('100', sol.addBinary('11', '1'))
        self.assertEqual('10101', sol.addBinary('1010', '1011'))


if __name__ == '__main__':
    unittest.main()
