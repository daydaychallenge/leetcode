import unittest
from most_common_word import Solution


class TestSolution(unittest.TestCase):
    def test_most_common_Solution(self):
        sol = Solution()
        paragrah = "Bob hit a ball, the hit BALL flew far after it was hit."
        self.assertEqual("ball", sol.mostCommonWord(paragrah, ['hit']))


if __name__ == '__main__':
    unittest.main()
