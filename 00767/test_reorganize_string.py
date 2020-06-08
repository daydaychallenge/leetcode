import unittest
from reorganize_string import Solution


class TestSolution(unittest.TestCase):
    def test_isValid_Solution(self):
        sol = Solution()
        self.assertEqual('aba', sol.reorganizeString('aab'))
        self.assertEqual('', sol.reorganizeString('aaab'))
        self.assertEqual('vovlv', sol.reorganizeString('vvolv'))


if __name__ == '__main__':
    unittest.main()
