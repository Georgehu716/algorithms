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
        if lst is None:
            return
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
    def is_valid_bst(self, root: Optional[TreeNode], left=-math.inf, right=math.inf) -> bool:
        if root is None:
            return True
        x = root.val
        return left < x < right and \
            self.is_valid_bst(root.left, left, x) and \
            self.is_valid_bst(root.right, x, right)


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_is_valid_bst(self):
        root = TreeNode.from_lst([2, 1, 3])
        result = self.solution.is_valid_bst(root)
        self.assertTrue(result)


if __name__ == "__main__":
    unittest.main()
