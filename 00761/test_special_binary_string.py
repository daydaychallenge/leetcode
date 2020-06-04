import unittest
from special_binary_string import Solution


class TestSolution(unittest.TestCase):
    def test_isValid_Solution(self):
        sol = Solution()
        self.assertEqual("11100100", sol.makeLargestSpecial("11011000"))


if __name__ == '__main__':
    unittest.main()
