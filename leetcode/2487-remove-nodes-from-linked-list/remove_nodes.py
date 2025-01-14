import unittest
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    @staticmethod
    def from_lst(lst):
        dummy = cur = ListNode()
        for val in lst:
            cur.next = ListNode(val)
            cur = cur.next
        return dummy.next

    def to_list(self):
        result = []
        cur = self
        while cur:
            result.append(cur.val)
            cur = cur.next
        return result


class Solution:
    def remove_nodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head = self.reverse_list(head)
        while cur.next:
            if cur.val > cur.next.val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return self.reverse_list(head)

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

    def test_remove_nodes(self):
        head = ListNode.from_lst([5, 2, 13, 3, 8])
        result = self.solution.remove_nodes(head)
        self.assertEqual(result.to_list(), [13, 8])

        head = ListNode.from_lst([1, 1, 1, 1])
        result = self.solution.remove_nodes(head)
        self.assertEqual(result.to_list(), [1, 1, 1, 1])


if __name__ == "__main__":
    unittest.main()
