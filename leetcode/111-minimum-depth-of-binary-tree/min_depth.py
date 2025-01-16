import math
import unittest
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    @staticmethod
    def from_lst(lst):
        if not lst:
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
    def min_depth(self, root: Optional[TreeNode]) -> int:
        ans = math.inf
        def dfs(node: Optional[TreeNode], cnt: int) -> None:
            if node is None:
                return
            nonlocal ans
            cnt += 1
            if cnt >= ans:
                return
            if node.left is node.right:
                ans = cnt
                return
            dfs(node.left, cnt)
            dfs(node.right, cnt)
        dfs(root, 0)
        return ans if root else 0


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_min_depth(self):
        root = TreeNode.from_lst([3, 9, 20, None, None, 15, 7])
        result = self.solution.min_depth(root)
        self.assertEqual(result, 2)


if __name__ == "__main__":
    unittest.main()
