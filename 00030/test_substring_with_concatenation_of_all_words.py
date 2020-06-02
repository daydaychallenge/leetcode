import unittest
from substring_with_concatenation_of_all_words import Solution


class TestSolution(unittest.TestCase):
    def test_isValid_Solution(self):
        sol = Solution()
        self.assertEqual([0, 9], sol.findSubstring("barfoothefoobarman", ["foo", "bar"]))
        self.assertEqual([], sol.findSubstring("wordgoodgoodgoodbestword", ["word", "good", "best", "word"]))
        self.assertEqual([8], sol.findSubstring("wordgoodgoodgoodbestword", ["word", "good", "best", "good"]))


if __name__ == '__main__':
    unittest.main()
