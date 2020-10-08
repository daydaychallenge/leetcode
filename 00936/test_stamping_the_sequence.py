import unittest
from stamping_the_sequence import Solution


class TestSolution(unittest.TestCase):
    def test_generateParenthesis_Solution(self):
        sol = Solution()
        self.assertEqual([1, 0, 2], sol.movesToStamp("abc", "ababc"))
        self.assertEqual([2, 3, 0, 1], sol.movesToStamp("abca", "aabcaca"))


if __name__ == '__main__':
    unittest.main()
