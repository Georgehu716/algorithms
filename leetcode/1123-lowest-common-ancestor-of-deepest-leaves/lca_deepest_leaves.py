import unittest
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.right = right
        self.left = left

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

    def find(self, val):
        if self.val == val:
            return self
        if self.left:
            found = self.left.find(val)
            if found:
                return found
        if self.right:
            found = self.right.find(val)
            if found:
                return found
        return None


class Solution:
    def lca_deepest_leaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        ans = None
        max_depth = -1
        def dfs(node: Optional[TreeNode], depth: int) -> int:
            nonlocal ans, max_depth
            if node is None:
                max_depth = max(max_depth, depth)
                return depth
            left_max_depth = dfs(node.left, depth + 1)
            right_max_depth = dfs(node.right, depth + 1)
            if left_max_depth == right_max_depth == max_depth:
                ans = node
            return max(left_max_depth, right_max_depth)
        dfs(root, 0)
        return ans


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_lca_deepest_leaves(self):
        root = TreeNode.from_lst([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])
        result = self.solution.lca_deepest_leaves(root)
        self.assertEqual(result, root.find(2))


if __name__ == "__main__":
    unittest.main()
