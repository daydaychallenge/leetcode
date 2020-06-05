import unittest
from first_unique_character_in_a_string import Solution


class TestSolution(unittest.TestCase):
    def test_isValid_Solution(self):
        sol = Solution()
        self.assertEqual(0, sol.firstUniqChar("leetcode"))
        self.assertEqual(2, sol.firstUniqChar("loveleetcode"))


if __name__ == '__main__':
    unittest.main()
