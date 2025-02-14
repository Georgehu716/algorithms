import unittest
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

    def get_next_values(self):
        result = []
        queue = [self]
        while queue:
            level_size = len(queue)
            level_values = []
            for i in range(level_size):
                node = queue.pop(0)
                level_values.append(node.next.val if node.next else None)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(level_values)
        return result

    @staticmethod
    def from_lst(lst):
        if lst is None:
            return None
        nodes = [TreeNode(val) if val is not None else None for val in lst]
        kids = nodes[::-1]
        root = kids.pop()
        for node in nodes:
            if node:
                if kids:
                    node.left = kids.pop()
                if kids:
                    node.right = kids.pop()
        return root


class Solution:
    def connect(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return root
        cur = [root]
        while cur:
            nxt = []
            cur_len = len(cur)
            for i in range(cur_len):
                if cur[i].left:
                    nxt.append(cur[i].left)
                if cur[i].right:
                    nxt.append(cur[i].right)
                if i < cur_len - 1:
                    cur[i].next = cur[i + 1]
                else:
                    cur[i].next = None
            cur = nxt
        return root


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_connect(self):
        root = TreeNode.from_lst([1, 2, 3, 4, 5, 6, 7])
        result = self.solution.connect(root)
        self.assertEqual(result.get_next_values(), [[None], [3, None], [5, 6, 7, None]])


if __name__ == "__main__":
    unittest.main()
