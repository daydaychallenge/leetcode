import unittest
from number_of_segments_in_a_string import Solution


class TestSolution(unittest.TestCase):
    def test_Calculate_Solution(self):
        sol = Solution()
        self.assertEqual(5, sol.countSegments("Hello, my name is John"))
        self.assertEqual(1, sol.countSegments("Hello"))
        self.assertEqual(4, sol.countSegments("love live! mu'sic forever"))


if __name__ == '__main__':
    unittest.main()
