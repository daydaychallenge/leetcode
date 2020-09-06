import unittest
from minimum_number_of_frogs_croaking import Solution


class TestSolution(unittest.TestCase):
    def test_Calculate_Solution(self):
        sol = Solution()
        self.assertEqual(1, sol.minNumberOfFrogs('croakcroak'))
        self.assertEqual(2, sol.minNumberOfFrogs('crcoakroak'))
        self.assertEqual(-1, sol.minNumberOfFrogs('croakcrook'))


if __name__ == '__main__':
    unittest.main()
