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
    def delete_duplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        cur = head
        while cur.next:
            if cur.next.val == cur.val:
                cur.next = cur.next.next
            else:
                cur = cur.next

        return head


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_delete_duplicates(self):
        head = ListNode.from_lst([1, 1, 2])
        result = self.solution.delete_duplicates(head)
        self.assertEqual(result.to_list(), [1, 2])

        head = ListNode.from_lst([1, 1, 2, 3, 3])
        result = self.solution.delete_duplicates(head)
        self.assertEqual(result.to_list(), [1, 2, 3])


if __name__ == "__main__":
    unittest.main()
