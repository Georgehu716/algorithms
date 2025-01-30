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
    def range_sum_bst(self, root: Optional[TreeNode], low: int, high: int) -> int:
        ans = 0
        def dfs(node: Optional[TreeNode]) -> None:
            if node is None:
                return
            if low <= node.val <= high:
                nonlocal ans
                ans += node.val
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return ans


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_range_sum_bst(self):
        root = TreeNode.from_lst([10, 5, 15, 3, 7, None, 18])
        result = self.solution.range_sum_bst(root, 7, 15)
        self.assertEqual(result, 32)


if __name__ == "__main__":
    unittest.main()
