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
    def right_side_view(self, root: Optional[TreeNode]) -> list[int]:
        ans = []
        nums = {}
        def dfs(node: Optional[TreeNode], level) -> None:
            if node is None:
                return
            nonlocal nums
            nums.setdefault(level, []).append(node.val)
            dfs(node.left, level + 1)
            dfs(node.right, level + 1)
        dfs(root, 0)
        for k, v in nums.items():
            ans.append(v[-1])
        return ans


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def test_right_side_view(self):
        root = TreeNode.from_lst([1, 2, 3, None, 5, None, 4])
        result = self.solution.right_side_view(root)
        self.assertEqual(result, [1, 3, 4])


if __name__ == "__main__":
    unittest.main()
