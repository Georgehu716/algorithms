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
    def find_bottom_left_value(self, root: Optional[TreeNode]) -> int:
        ans = []
        cur = [root]
        while cur:
            vals = []
            nxt = []
            for node in cur:
                vals.append(node.val)
                if node.left: nxt.append(node.left)
                if node.right: nxt.append(node.right)
            cur = nxt
            ans.append(vals)
        return ans[-1][0]


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_find_bottom_left_value(self):
        root = TreeNode.from_lst([2, 1, 3])
        result = self.solution.find_bottom_left_value(root)
        self.assertEqual(result, 1)


if __name__ == "__main__":
    unittest.main()
