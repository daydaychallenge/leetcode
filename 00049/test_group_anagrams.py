import unittest
from group_anagrams import Solution


class TestSolution(unittest.TestCase):
    def test_isValid_Solution(self):
        sol = Solution()
        self.assertEqual(
            [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]],
            sol.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))


if __name__ == '__main__':
    unittest.main()
