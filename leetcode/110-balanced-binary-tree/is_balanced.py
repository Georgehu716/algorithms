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
    def is_balanced(self, root: Optional[TreeNode]) -> bool:
        def get_height(node: Optional[TreeNode]) -> int:
            if node is None:
                return 0
            l_h = get_height(node.left)
            if l_h == -1:
                return -1
            r_h = get_height(node.right)
            if r_h == -1 or abs(l_h - r_h) > 1:
                return -1
            return max(l_h, r_h) + 1
        return get_height(root) != -1


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_is_balanced(self):
        root = TreeNode.from_lst([3, 9, 20, None, None, 15, 7])
        result = self.solution.is_balanced(root)
        self.assertTrue(result)


if __name__ == "__main__":
    unittest.main()
