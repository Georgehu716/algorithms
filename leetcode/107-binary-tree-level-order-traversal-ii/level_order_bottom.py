import unittest
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

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
    def level_order_bottom(self, root: Optional[TreeNode]) -> list[list[int]]:
        if root is None:
            return []
        ans = []
        cur = [root]
        while cur:
            nxt = []
            vals = []
            for node in cur:
                vals.append(node.val)
                if node.left: nxt.append(node.left)
                if node.right: nxt.append(node.right)
            cur = nxt
            ans.append(vals)
        return ans[::-1]


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_level_order_bottom(self):
        root = TreeNode.from_lst([3, 9, 20, None, None, 15, 7])
        result = self.solution.level_order_bottom(root)
        self.assertEqual(result, [[15, 7], [9, 20], [3]])


if __name__ == "__main__":
    unittest.main()
