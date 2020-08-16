import unittest
from construct_string_from_binary_tree import Solution, TreeNode


class TestSolution(unittest.TestCase):
    def test_isValid_Solution(self):
        sol = Solution()
        #       1
        #     /   \
        #    2     3
        #     \
        #      4

        one = TreeNode(1)
        two = TreeNode(2)
        three = TreeNode(3)
        four = TreeNode(4)
        one.left = two
        one.right = three
        two.right = four

        self.assertEqual("1(2()(4))(3)", sol.tree2str(one))


if __name__ == '__main__':
    unittest.main()
