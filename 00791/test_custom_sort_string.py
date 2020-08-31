import unittest
from custom_sort_string import Solution


class TestSolution(unittest.TestCase):
    def test_custom_sort_string_Solution(self):
        sol = Solution()
        self.assertEqual('cbad', sol.customSortString('cba', 'abcd'))


if __name__ == '__main__':
    unittest.main()
