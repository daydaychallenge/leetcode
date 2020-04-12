import unittest
from check_if_word_is_valid_after_substitutions import Solution


class TestSolution(unittest.TestCase):
    def test_isValid_Solution(self):
        sol = Solution()
        self.assertTrue(sol.isValid('aabcbc'))
        self.assertTrue(sol.isValid('abcabcababcc'))
        self.assertFalse(sol.isValid('abccba'))
        self.assertFalse(sol.isValid('cababc'))


if __name__ == '__main__':
    unittest.main()
