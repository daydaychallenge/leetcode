import unittest
from length_of_last_word import Solution


class TestSolution(unittest.TestCase):
    def test_isValid_Solution(self):
        sol = Solution()
        self.assertEqual(5, sol.lengthOfLastWord("hello  world   "))
        self.assertEqual(5, sol.lengthOfLastWordV01("hello  world   "))


if __name__ == '__main__':
    unittest.main()
