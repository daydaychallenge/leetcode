import unittest
from invalid_transactions import Solution


class TestSolution(unittest.TestCase):
    def test_generateParenthesis_Solution(self):
        sol = Solution()
        self.assertEqual(
            ["alice,20,800,mtv", "alice,50,100,beijing"],
            sol.invalidTransactions(["alice,20,800,mtv", "alice,50,100,beijing"])
        )
        self.assertEqual(
            ["alice,50,1200,mtv"],
            sol.invalidTransactions(["alice,20,800,mtv", "alice,50,1200,mtv"])
        )
        self.assertEqual(
            ["bob,50,1200,mtv"],
            sol.invalidTransactions(["alice,20,800,mtv", "bob,50,1200,mtv"])
        )


if __name__ == '__main__':
    unittest.main()
