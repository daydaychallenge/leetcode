import unittest
from count_and_say import Solution


class TestSolution(unittest.TestCase):
    def test_Calculate_Solution(self):
        sol = Solution()
        self.assertEqual('1', sol.countAndSay(1))
        self.assertEqual('11', sol.countAndSay(2))
        self.assertEqual('21', sol.countAndSay(3))
        self.assertEqual('1211', sol.countAndSay(4))
        self.assertEqual('111221', sol.countAndSay(5))


if __name__ == '__main__':
    unittest.main()
