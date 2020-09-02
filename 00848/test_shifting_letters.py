import unittest
from shifting_letters import Solution


class TestSolution(unittest.TestCase):
    def test_isValid_Solution(self):
        sol = Solution()
        self.assertEqual('rpl', sol.shiftingLetters('abc', [3, 5, 9]))


if __name__ == '__main__':
    unittest.main()
