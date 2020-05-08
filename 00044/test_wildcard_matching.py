import unittest
from wildcard_matching import Solution


class TestSolution(unittest.TestCase):
    def test_isValid_Solution(self):
        sol = Solution()
        self.assertTrue(sol.isMatch("aa", "*"))
        self.assertFalse(sol.isMatch("aa", "a"))
        self.assertFalse(sol.isMatch("cb", "?a"))
        self.assertTrue(sol.isMatch("adceb", "*a*b"))
        self.assertTrue(sol.isMatch("accccb", "a*cb"))
        self.assertFalse(sol.isMatch("acdcb", "a*c?b"))


if __name__ == '__main__':
    unittest.main()
