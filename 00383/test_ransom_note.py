import unittest
from ransom_note import Solution


class TestSolution(unittest.TestCase):
    def test_isValid_Solution(self):
        sol = Solution()
        self.assertTrue(sol.canConstruct("aa", "aab"))
        self.assertFalse(sol.canConstruct("aa", "ab"))


if __name__ == '__main__':
    unittest.main()
