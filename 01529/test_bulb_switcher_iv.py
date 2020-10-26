import unittest
from bulb_switcher_iv import Solution


class TestSolution(unittest.TestCase):
    def test_generateParenthesis_Solution(self):
        sol = Solution()
        self.assertEqual(3, sol.minFlips("10111"))
        self.assertEqual(3, sol.minFlips("101"))
        self.assertEqual(0, sol.minFlips("00000"))
        self.assertEqual(5, sol.minFlips("001011101"))


if __name__ == '__main__':
    unittest.main()
