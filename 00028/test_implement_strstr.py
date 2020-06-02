import unittest
from implement_strstr import Solution


class TestSolution(unittest.TestCase):
    def test_isValid_Solution(self):
        sol = Solution()
        self.assertEqual(2, sol.strStr("hello", "ll"))
        self.assertEqual(-1, sol.strStr("aaaaa", "bba"))
        self.assertEqual(0, sol.strStr("", ""))
        self.assertEqual(15, sol.strStr("bbc abcdab abcdabcdabde", "abcdabd"))

        self.assertEqual(2, sol.strRabinKarp("hello", "ll"))
        self.assertEqual(-1, sol.strRabinKarp("aaaaa", "bba"))
        self.assertEqual(0, sol.strRabinKarp("", ""))
        self.assertEqual(15, sol.strRabinKarp("bbc abcdab abcdabcdabde", "abcdabd"))


if __name__ == '__main__':
    unittest.main()
