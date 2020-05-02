import unittest
from longest_common_prefix import Solution


class TestSolution(unittest.TestCase):
    def test_Calculate_Solution(self):
        sol = Solution()
        self.assertEqual('fl', sol.longestCommonPrefix(['flower', 'flow', 'flight']))
        self.assertEqual('', sol.longestCommonPrefix(['dog', 'racecar', 'car']))


if __name__ == '__main__':
    unittest.main()
