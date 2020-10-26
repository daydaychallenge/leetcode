import unittest
from form_largest_integer_with_digits_that_add_up_to_target import Solution


class TestSolution(unittest.TestCase):
    def test_generateParenthesis_Solution(self):
        sol = Solution()
        self.assertEqual("7772", sol.largestNumber([4, 3, 2, 5, 6, 7, 2, 5, 5], 9))
        self.assertEqual("85", sol.largestNumber([7, 6, 5, 5, 5, 6, 8, 7, 8], 12))
        self.assertEqual("0", sol.largestNumber([2, 4, 6, 2, 4, 6, 4, 4, 4], 5))
        self.assertEqual("32211", sol.largestNumber([6, 10, 15, 40, 40, 40, 40, 40, 40], 47))


if __name__ == '__main__':
    unittest.main()
