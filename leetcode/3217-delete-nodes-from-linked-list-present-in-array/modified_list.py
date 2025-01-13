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
    def modified_list(self, nums: list[int], head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = cur = ListNode(next=head)
        ns = set(nums)
        while cur.next:
            if cur.next.val in ns:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return dummy.next


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_modified_list(self):
        nums = [1, 2, 3]
        head = ListNode.from_lst([1, 2, 3, 4, 5])
        result = self.solution.modified_list(nums, head)
        self.assertEqual(result.to_list(), [4, 5])


if __name__ == "__main__":
    unittest.main()
