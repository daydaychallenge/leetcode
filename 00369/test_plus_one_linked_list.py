import unittest
from plus_one_linked_list import Solution, ListNode


class TestSolution(unittest.TestCase):
    def test_generateParenthesis_Solution(self):
        sol = Solution()
        node1 = ListNode(1)
        node2 = ListNode(2)
        node3 = ListNode(3)
        node1.next = node2
        node2.next = node3

        head = sol.plusOne(node1)
        ret = 0
        while head:
            ret = ret*10 + head.val
            head = head.next

        self.assertEqual(124, ret)

        node1 = ListNode(9)
        node2 = ListNode(9)
        node3 = ListNode(9)
        node1.next = node2
        node2.next = node3

        head = sol.plusOne(node1)
        ret = 0
        while head:
            ret = ret*10 + head.val
            head = head.next

        self.assertEqual(1000, ret)


if __name__ == '__main__':
    unittest.main()
