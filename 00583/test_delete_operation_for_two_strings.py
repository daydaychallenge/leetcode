import unittest
from delete_operation_for_two_strings import Solution


class TestSolution(unittest.TestCase):
    def test_Calculate_Solution(self):
        sol = Solution()
        self.assertEqual(2, sol.minDistance("sea", "eat"))


if __name__ == '__main__':
    unittest.main()
