import unittest
from add_two_numbers_ii import Solution, ListNode


class TestSolution(unittest.TestCase):
    def test_generateParenthesis_Solution(self):
        sol = Solution()
        node1 = ListNode(1)
        node2 = ListNode(2)
        node3 = ListNode(3)
        node1.next = node2
        node2.next = node3

        mode1 = ListNode(9)
        mode2 = ListNode(9)
        mode3 = ListNode(9)
        mode1.next = mode2
        mode2.next = mode3

        head = sol.addTwoNumbers(node1, mode1)
        ret = []
        while head:
            ret.append(head.val)
            head = head.next

        self.assertEqual([1, 1, 2, 2], ret)


if __name__ == '__main__':
    unittest.main()
