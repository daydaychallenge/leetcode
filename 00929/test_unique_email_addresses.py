import unittest
from unique_email_addresses import Solution


class TestSolution(unittest.TestCase):
    def test_isValid_Solution(self):
        sol = Solution()
        self.assertEqual(2, sol.numUniqueEmails([
            "test.email+alex@leetcode.com",
            "test.e.mail+bob.cathy@leetcode.com",
            "testemail+david@lee.tcode.com"]
        ))


if __name__ == '__main__':
    unittest.main()
