import unittest
from simplify_path import Solution


class TestSolution(unittest.TestCase):
    def test_simplify_path(self):
        sol = Solution()
        self.assertEqual('/home', sol.simplifyPath('/home/'))
        self.assertEqual('/', sol.simplifyPath('/../'))
        self.assertEqual('/home/foo', sol.simplifyPath('/home//foo/'))
        self.assertEqual('/c', sol.simplifyPath('/a/./b/../../c/'))
        self.assertEqual('/c', sol.simplifyPath('/a/../../b/../c//.//'))
        self.assertEqual('/a/b/c', sol.simplifyPath('/a//b////c/d//././/..'))


if __name__ == '__main__':
    unittest.main()
