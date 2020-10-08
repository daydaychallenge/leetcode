import unittest
from remove_sub_folders_from_the_filesystem import Solution


class TestSolution(unittest.TestCase):
    def test_generateParenthesis_Solution(self):
        sol = Solution()
        self.assertEqual({"/a", "/c/d", "/c/f"}, set(sol.removeSubfolders(["/a", "/a/b", "/c/d", "/c/d/e", "/c/f"])))
        self.assertEqual({"/a"}, set(sol.removeSubfolders(["/a", "/a/b/c", "/a/b/d"])))
        self.assertEqual({"/a/b/c", "/a/b/ca", "/a/b/d"}, set(sol.removeSubfolders(["/a/b/c", "/a/b/ca", "/a/b/d"])))


if __name__ == '__main__':
    unittest.main()
