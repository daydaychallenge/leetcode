import unittest
from minimum_time_difference import Solution


class TestSolution(unittest.TestCase):
    def test_minRemoveToMakeValid(self):
        sol = Solution()
        self.assertEqual(1, sol.findMinDifference(["23:59", "00:00"]))
        self.assertEqual(0, sol.findMinDifference(["23:59", "00:00", "00:00"]))


if __name__ == '__main__':
    unittest.main()
