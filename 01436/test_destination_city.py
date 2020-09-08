import unittest
from destination_city import Solution


class TestSolution(unittest.TestCase):
    def test_Calculate_Solution(self):
        sol = Solution()
        self.assertEqual("Sao Paulo", sol.destCity([["London", "New York"], ["New York", "Lima"], ["Lima", "Sao Paulo"]]))
        self.assertEqual("A", sol.destCity([["B", "C"], ["D", "B"], ["C", "A"]]))


if __name__ == '__main__':
    unittest.main()
