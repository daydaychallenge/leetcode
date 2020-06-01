import unittest
from one_edit_distance import Solution


class TestSolution(unittest.TestCase):
    def test_isValid_Solution(self):
        sol = Solution()
        self.assertTrue(sol.isOneEditDistance("ab", "acb"))
        self.assertFalse(sol.isOneEditDistance("cab", "ad"))
        self.assertTrue(sol.isOneEditDistance("1203", "1213"))
        self.assertFalse(sol.isOneEditDistance("", ""))
        self.assertFalse(sol.isOneEditDistance("ab", "ab"))


if __name__ == '__main__':
    unittest.main()
