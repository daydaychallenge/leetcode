import unittest
from string_matching_in_an_array import Solution


class TestSolution(unittest.TestCase):
    def test_Calculate_Solution(self):
        sol = Solution()
        self.assertEqual(['as', 'hero'], sol.stringMatching(['mass', 'as', 'hero', 'superhero']))
        self.assertEqual(['et', 'code'], sol.stringMatching(['leetcode', 'et', 'code']))
        self.assertEqual([], sol.stringMatching(['blue', 'green', 'bu']))


if __name__ == '__main__':
    unittest.main()
