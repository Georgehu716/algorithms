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


class Solution:
    def is_palindrome(self, head: Optional[ListNode]) -> bool:
        mid = self.middle_node(head)
        head2 = self.reverse_list(mid)
        while head2:
            if head2.val != head.val:
                return False
            head2 = head2.next
            head = head.next
        return True

    def middle_node(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = slow = head

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

    def test_is_palindrome(self):
        head = ListNode.from_lst([1, 2, 2, 1])
        result = self.solution.is_palindrome(head)
        self.assertTrue(result)

        head = ListNode.from_lst([1, 2])
        result = self.solution.is_palindrome(head)
        self.assertFalse(result)


if __name__ == "__main__":
    unittest.main()
