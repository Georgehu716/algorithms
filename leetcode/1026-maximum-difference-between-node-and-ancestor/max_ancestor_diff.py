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
    def max_ancestor_diff(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def dfs(node: Optional[TreeNode], mn: int, mx: int) -> None:
            if node is None:
                return
            mn = min(mn, node.val)
            mx = max(mx, node.val)
            nonlocal ans
            ans = max(ans, node.val - mn, mx - node.val)
            dfs(node.left, mn, mx)
            dfs(node.right, mn, mx)
        dfs(root, root.val, root.val)
        return ans


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def test_max_ancestor_diff(self):
        root = TreeNode.from_lst([8, 3, 10, 1, 6, None, 14, None, None, 4, 7, 13])
        result = self.solution.max_ancestor_diff(root)
        self.assertEqual(result, 7)


if __name__ == "__main__":
    unittest.main()
