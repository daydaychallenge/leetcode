import unittest
from minimum_swaps_to_make_strings_equal import Solution


class TestSolution(unittest.TestCase):
    def test_generateParenthesis_Solution(self):
        sol = Solution()
        self.assertEqual(1, sol.minimumSwap('xx', 'yy'))
        self.assertEqual(2, sol.minimumSwap('xy', 'yx'))
        self.assertEqual(-1, sol.minimumSwap('xx', 'yx'))
        self.assertEqual(4, sol.minimumSwap("xxyyxyxyxx", "xyyxyxxxyx"))


if __name__ == '__main__':
    unittest.main()
