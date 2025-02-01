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
    def kth_smallest(self, root: Optional[TreeNode], k: int) -> int:
        def dfs(node: Optional[TreeNode]):
            if node is None:
                return -1
            left_res = dfs(node.left)
            if left_res != -1:
                return left_res
            nonlocal k
            k -= 1
            if k == 0:
                return node.val
            return dfs(node.right)
        return dfs(root)


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_kth_smallest(self):
        root = TreeNode.from_lst([3, 1, 4, None, 2])
        result = self.solution.kth_smallest(root, 1)
        self.assertEqual(result, 1)


if __name__ == "__main__":
    unittest.main()
