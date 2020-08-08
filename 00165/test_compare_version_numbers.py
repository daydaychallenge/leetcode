import unittest
from compare_version_numbers import Solution


class TestSolution(unittest.TestCase):
    def test_generateParenthesis_Solution(self):
        sol = Solution()
        self.assertEqual(-1, sol.compareVersion('0.1', '1.1'))
        self.assertEqual(1, sol.compareVersion('1.0.1', '1'))
        self.assertEqual(-1, sol.compareVersion('7.5.2.4', '7.5.3'))


if __name__ == '__main__':
    unittest.main()
