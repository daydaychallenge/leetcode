import unittest
from word_abbreviation import Solution


class TestSolution(unittest.TestCase):
    def test_generateParenthesis_Solution(self):
        sol = Solution()
        self.assertEqual(
            ["l2e", "god", "internal", "me", "i6t", "interval", "inte4n", "f2e", "intr4n"],
            sol.wordsAbbreviation(
                ["like", "god", "internal", "me", "internet", "interval", "intension", "face", "intrusion"]
            )
        )


if __name__ == '__main__':
    unittest.main()
