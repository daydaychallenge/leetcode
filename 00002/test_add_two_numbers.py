import unittest
from add_two_numbers import Solution, ListNode


class TestSolution(unittest.TestCase):
    def test_isValid_Solution(self):
        sol = Solution()
        node12 = ListNode(2)
        node14 = ListNode(4)
        node13 = ListNode(3)
        node12.next = node14
        node14.next = node13

        node25 = ListNode(5)
        node26 = ListNode(6)
        node24 = ListNode(4)
        node25.next = node26
        node26.next = node24

        head = sol.addTwoNumbers(node12, node25)

        def _gen(node):
            while node:
                yield node.val
                node = node.next

        self.assertEqual([7, 0, 8], list(_gen(head)))


if __name__ == '__main__':
    unittest.main()
