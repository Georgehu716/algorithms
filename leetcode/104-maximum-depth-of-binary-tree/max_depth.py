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
    def max_depth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        l_depth = self.max_depth(root.left)
        r_depth = self.max_depth(root.right)
        return max(l_depth, r_depth) + 1


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_max_depth(self):
        root = TreeNode.from_lst([3, 9, 20, None, None, 15, 7])
        result = self.solution.max_depth(root)
        self.assertEqual(result, 3)


if __name__ == "__main__":
    unittest.main()
