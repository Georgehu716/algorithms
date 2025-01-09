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
    def remove_nth_from_end(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        left = right = dummy = ListNode(next=head)
        for _ in range(n):
            right = right.next
        while right.next:
            right = right.next
            left = left.next

        left.next = left.next.next
        return dummy.next


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_remove_nth_from_end(self):
        head = ListNode.from_lst([1, 2, 3, 4, 5])
        result = self.solution.remove_nth_from_end(head, 2)
        self.assertEqual(result.to_list(), [1, 2, 3, 5])

        head = ListNode.from_lst([1])
        result = self.solution.remove_nth_from_end(head, 1)
        self.assertEqual(result, None)

        head = ListNode.from_lst([1, 2])
        result = self.solution.remove_nth_from_end(head, 2)
        self.assertEqual(result.to_list(), [2])

        head = ListNode.from_lst([1, 2])
        result = self.solution.remove_nth_from_end(head, 1)
        self.assertEqual(result.to_list(), [1])


if __name__ == "__main__":
    unittest.main()
