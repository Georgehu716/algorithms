import unittest
from typing import Optional


# Definition of singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    @staticmethod
    def from_list(lst):
        dummy = ListNode()
        cur = dummy
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
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow


class TestSolution:
    def setUp(self):
        self.solution = Solution()

    def test_middleNode(self):
        head = ListNode.from_lst([1, 2, 3, 4, 5])
        result = self.solution.middleNode(head)
        self.assertEqual(result.to_list(), [3, 4, 5])

        head = ListNode.from_lst([1, 2, 3, 4, 5, 6])
        result = self.solution.middleNode(head)
        self.assertEqual(result.to_list(), [4, 5, 6])


if __name__ == "__main__":
    unittest.main()
