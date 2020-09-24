import unittest
from number_of_substrings_containing_all_three_characters import Solution


class TestSolution(unittest.TestCase):
    def test_minRemoveToMakeValid(self):
        sol = Solution()
        self.assertEqual(10, sol.numberOfSubstrings("abcabc"))
        self.assertEqual(3, sol.numberOfSubstrings("aaacb"))


if __name__ == '__main__':
    unittest.main()
