import unittest
from longest_happy_prefix import Solution


class TestSolution(unittest.TestCase):
    def test_Calculate_Solution(self):
        sol = Solution()
        self.assertEqual("l", sol.longestPrefix("level"))
        self.assertEqual("abab", sol.longestPrefix("ababab"))
        self.assertEqual("leet", sol.longestPrefix("leetcodeleet"))
        self.assertEqual("", sol.longestPrefix("a"))

        self.assertEqual("l", sol.longestPrefix_KMP("level"))
        self.assertEqual("abab", sol.longestPrefix_KMP("ababab"))
        self.assertEqual("leet", sol.longestPrefix_KMP("leetcodeleet"))
        self.assertEqual("", sol.longestPrefix_KMP("a"))

if __name__ == '__main__':
    unittest.main()
