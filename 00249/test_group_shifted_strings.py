import unittest
from group_shifted_strings import Solution


class TestSolution(unittest.TestCase):
    def test_isValid_Solution(self):
        sol = Solution()
        result = [
            ["abc", "bcd", "xyz"], ["acef"],
            ["az", "ba"], ["a", "z"]
        ]
        test_result = sol.groupStrings(["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"])
        self.assertEqual(sorted(result), sorted(test_result))


if __name__ == '__main__':
    unittest.main()
