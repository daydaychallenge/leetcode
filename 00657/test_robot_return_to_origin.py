import unittest
from robot_return_to_origin import Solution


class TestSolution(unittest.TestCase):
    def test_isValid_Solution(self):
        sol = Solution()
        self.assertTrue(sol.judgeCircle("UD"))
        self.assertFalse(sol.judgeCircle("LL"))


if __name__ == '__main__':
    unittest.main()
