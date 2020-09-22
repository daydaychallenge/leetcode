import unittest
from expressive_words import Solution


class TestSolution(unittest.TestCase):
    def test_Calculate_Solution(self):
        sol = Solution()
        self.assertEqual(1, sol.expressiveWords("heeellooo", ["hello", "hi", "helo"]))


if __name__ == '__main__':
    unittest.main()
