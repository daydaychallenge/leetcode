import unittest
from valid_anagram import Solution


class TestSolution(unittest.TestCase):
    def test_isValid_Solution(self):
        sol = Solution()
        self.assertTrue(sol.isAnagram("anagram", "nagaram"))
        self.assertFalse(sol.isAnagram("rat", "car"))


if __name__ == '__main__':
    unittest.main()
