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
    def is_same_tree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None or q is None:
            return p is q
        return p.val == q.val and self.is_same_tree(p.left, q.left) and self.is_same_tree(p.right, q.right)


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_is_same_tree(self):
        p = TreeNode.from_lst([1, 2, 3])
        q = TreeNode.from_lst([1, 2, 3])
        result = self.solution.is_same_tree(p, q)
        self.assertTrue(result)


if __name__ == "__main__":
    unittest.main()
