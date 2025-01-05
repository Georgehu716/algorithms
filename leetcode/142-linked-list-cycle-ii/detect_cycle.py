import unittest
from typing import Optional, Self


# Definition for singly-linked list
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    @staticmethod
    def from_lst(lst: list[int], pos: int) -> Optional[Self]:
        dummy = p = ListNode
        cycle = None
        for idx, val in enumerate(lst):
            p.next = ListNode(val)
            if pos >= 0 and idx == pos:
                cycle = p.next
            p = p.next
        p.next = cycle
        return dummy.next

    def to_list(self) -> list[int]:
        result = []
        cur = self
        while cur:
            result.append(cur.val)
            cur = cur.next
        return result


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = slow = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

            if fast is slow:
                while slow is not head:
                    slow = slow.next
                    head = head.next
                return slow
        return None


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_detect_cycle(self):
        head = ListNode.from_lst([3, 2, 0, -4], 1)
        result = self.solution.detectCycle(head)
        self.assertEqual(result, head.next)

        head = ListNode.from_lst([1], -1)
        result = self.solution.detectCycle(head)
        self.assertEqual(result, None)

if __name__ == "__main__":
    unittest.main()
