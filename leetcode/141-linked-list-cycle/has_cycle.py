import unittest
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    @staticmethod
    def from_lst(lst, pos):
        """Convert a list into a linked list"""
        dummy = cur = ListNode()
        cycle = None
        for idx, val in enumerate(lst):
            cur.next = ListNode(val)
            if pos >= 0 and idx == pos:
                cycle = cur.next
            cur = cur.next
        cur.next = cycle
        return dummy.next
	
    def to_list(self):
        result = []
        cur = self
        while cur:
            result.append(cur.val)
        cur = cur.next
        return result


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast = slow = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast is slow:
                return True
        return False


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_hasCycle(self):
        head = ListNode.from_lst([3, 2, 0, -4], 1)
        result = self.solution.hasCycle(head)
        self.assertEqual(result, True)

        head = ListNode.from_lst([1, 2], 0)
        result = self.solution.hasCycle(head)
        self.assertEqual(result, True)

        head = ListNode.from_lst([1], -1)
        result = self.solution.hasCycle(head)
        self.assertEqual(result, False)

if __name__ == "__main__":
    unittest.main()
