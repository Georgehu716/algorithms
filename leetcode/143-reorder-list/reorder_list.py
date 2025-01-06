import unittest
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    @staticmethod
    def from_lst(lst):
        dummy = p = ListNode()
        for val in lst:
            p.next = ListNode(val)
            p = p.next
        return dummy.next

    def to_list(self):
        result = []
        cur = self
        while cur:
            result.append(cur.val)
            cur = cur.next
        return result


class Solution:
    def reorder_list(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Do not return anything, modify head in-place instead.
        """
        mid = self.middle_node(head)
        head2 = self.reverse_list(mid)
        while head2.next:
            nxt = head.next
            nxt2 = head2.next
            head.next = head2
            head2.next = nxt
            head = nxt
            head2 = nxt2

    def middle_node(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def reverse_list(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pre, cur = None, head
        while cur:
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt
        return pre


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_reorder_list(self):
        head = ListNode.from_lst([1, 2, 3, 4])
        self.solution.reorder_list(head)
        self.assertEqual(head.to_list(), [1, 4, 2, 3])

        head = ListNode.from_lst([1, 2, 3, 4, 5])
        self.solution.reorder_list(head)
        self.assertEqual(head.to_list(), [1, 5, 2, 4, 3])


if __name__ == "__main__":
    unittest.main()
