import unittest
from next_greater_element_iii import Solution


class TestSolution(unittest.TestCase):
    def test_generateParenthesis_Solution(self):
        sol = Solution()
        self.assertEqual(21, sol.nextGreaterElement(12))


if __name__ == '__main__':
    unittest.main()
