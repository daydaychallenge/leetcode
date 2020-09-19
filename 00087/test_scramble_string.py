import unittest
from scramble_string import Solution


class TestSolution(unittest.TestCase):
    def test_minRemoveToMakeValid(self):
        sol = Solution()
        self.assertTrue(sol.isScramble("great", "rgeat"))
        self.assertFalse(sol.isScramble("abcde", "caebd"))


if __name__ == '__main__':
    unittest.main()
