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
    def good_nodes(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def dfs(node: Optional[TreeNode], max_num) -> None:
            if node is None:
                return
            if node.val >= max_num:
                max_num = node.val
                nonlocal ans
                ans += 1
            dfs(node.left, max_num)
            dfs(node.right, max_num)

        dfs(root, root.val)
        return ans


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_good_nodes(self):
        root = TreeNode.from_lst([3, 1, 4, 3, None, 1, 5])
        result = self.solution.good_nodes(root)
        self.assertEqual(result, 4)


if __name__ == "__main__":
    unittest.main()
