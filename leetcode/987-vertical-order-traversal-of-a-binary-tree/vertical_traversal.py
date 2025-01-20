import unittest
from typing import Optional
from collections import defaultdict


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
    def vertical_traversal(self, root: Optional[TreeNode]) -> list[list[int]]:
        groups = defaultdict(list)
        def dfs(node: Optional[TreeNode], row: int, col: int):
            if node is None:
                return
            groups[col].append((row, node.val))
            dfs(node.left, row + 1, col - 1)
            dfs(node.right, row + 1, col + 1)
        dfs(root, 0, 0)

        ans = []
        for _, g in sorted(groups.items()):
            g.sort()
            ans.append([val for _, val in g])
        return ans


class TestSolution:
    def setUp(self):
        self.solution = Solution()

    def test_vertical_traversal(self):
        root = TreeNode.from_lst([3, 9, 20, None, None, 15, 7])
        result = self.solution.vertical_traversal(root)
        self.assertEqual(result, [[9], [3, 15], [20], [7]])


if __name__ == "__main__":
    unittest.main()
