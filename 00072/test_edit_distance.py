import unittest
from edit_distance import Solution


class TestSolution(unittest.TestCase):
    def test_isValid_Solution(self):
        sol = Solution()
        self.assertEqual(3, sol.minDistance("horse", "ros"))
        self.assertEqual(5, sol.minDistance("intention", "execution"))


if __name__ == '__main__':
    unittest.main()
