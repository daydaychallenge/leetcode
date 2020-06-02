import unittest
from unique_morse_code_words import Solution


class TestSolution(unittest.TestCase):
    def test_isValid_Solution(self):
        sol = Solution()
        self.assertEqual(2, sol.uniqueMorseRepresentations(["gin", "zen", "gig", "msg"]))


if __name__ == '__main__':
    unittest.main()
