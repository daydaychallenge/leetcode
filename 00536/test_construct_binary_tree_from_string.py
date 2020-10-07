import unittest
from construct_binary_tree_from_string import Solution, TreeNode


class TestSolution(unittest.TestCase):
    def test_generateParenthesis_Solution(self):
        sol = Solution()
        root1 = TreeNode(4)
        node2 = TreeNode(2)
        node6 = TreeNode(6)
        node3 = TreeNode(3)
        node1 = TreeNode(1)
        node5 = TreeNode(5)
        root1.left = node2
        root1.right = node6
        node2.left = node3
        node2.right = node1
        node6.left = node5

        root2 = sol.str2tree("4(2(3)(1))(6(5))")

        def is_equal_tree(r1, r2):
            if r1 is None and r2 is None:
                return True

            if not r1 or not r2 or r1.val != r2.val:
                return False

            return is_equal_tree(r1.left, r2.left) and is_equal_tree(r1.right, r2.right)

        self.assertTrue(is_equal_tree(root1, root2))


if __name__ == '__main__':
    unittest.main()
