import unittest
from typing import Optional


# Definition for singly-linked list
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    # Helper method to convert a list into a linked list @staticmethod
    def from_list(lst):
        dummy = ListNode()
        cur = dummy
        for value in lst:
            cur.next = ListNode(value)
            cur = cur.next
        return dummy.next

    # Helper method to convert a linked list back to list
    def to_list(self):
        result = []
        cur = self
        while cur:
            result.append(cur.val)
            cur = cur.next
        return result


class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.val > 4:
            head = ListNode(0, head)
        cur = head
        while cur:
            cur.val = cur.val * 2 % 10
            if cur.next and cur.next.val > 4:
                cur.val += 1
            cur = cur.next
        return head


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_doubleIt(self):
        head = ListNode.from_list([1, 8, 9])
        result = self.solution.doubleIt(head)
        self.assertEqual(result.to_list(), [3, 7, 8])

        head = ListNode.from_list([9, 9, 9])
        result = self.solution.doubleIt(head)
        self.assertEqual(result.to_list(), [1, 9, 9, 8])


if __name__ == "__main__":
    unittest.main()
