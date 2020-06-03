import unittest
from add_strings import Solution


class TestSolution(unittest.TestCase):
    def test_isValid_Solution(self):
        sol = Solution()
        self.assertEqual('200', sol.addStrings('1', '199'))
        self.assertEqual('100', sol.addStrings('1', '99'))


if __name__ == '__main__':
    unittest.main()
