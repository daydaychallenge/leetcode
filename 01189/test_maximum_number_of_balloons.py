import unittest
from maximum_number_of_balloons import Solution


class TestSolution(unittest.TestCase):
    def test_generateParenthesis_Solution(self):
        sol = Solution()
        self.assertEqual(1, sol.maxNumberOfBalloons("nlaebolko"))
        self.assertEqual(2, sol.maxNumberOfBalloons("loonbalxballpoon"))
        self.assertEqual(0, sol.maxNumberOfBalloons("leetcode"))


if __name__ == '__main__':
    unittest.main()
