import unittest
from remove_comments import Solution


class TestSolution(unittest.TestCase):
    def test_remove_comments(self):
        sol = Solution()
        source = [
            "/*Test program */", "int main()", "{ ",
            "  // variable declaration ", "int a, b, c;",
            "/* This is a test", "   multiline  ",
            "   comment for ", "   testing */", "a = b + c;", "}"
        ]
        target = ["int main()", "{ ", "  ", "int a, b, c;", "a = b + c;", "}"]
        self.assertEqual(target, sol.removeComments(source))

        source = ["a/*comment", "line", "more_comment*/b"]
        target = ["ab"]
        self.assertEqual(target, sol.removeComments(source))


if __name__ == '__main__':
    unittest.main()
