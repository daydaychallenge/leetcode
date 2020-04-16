import unittest
from reverse_string_ii import Solution


class TestSolution(unittest.TestCase):
    def test_isValid_Solution(self):
        sol = Solution()
        self.assertEqual('bacdfeg', sol.reverseStr('abcdefg', 2))


if __name__ == '__main__':
    unittest.main()
