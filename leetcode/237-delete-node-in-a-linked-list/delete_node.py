import unittest


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
    def delete_node(self, node):
        node.val = node.next.val
        node.next = node.next.next


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_delete_node(self):
        head = ListNode.from_lst([4, 5, 1, 9])
        self.solution.delete_node(head.next)
        self.assertEqual(head.to_list(), [4, 1, 9])


if __name__ == "__main__":
    unittest.main()
