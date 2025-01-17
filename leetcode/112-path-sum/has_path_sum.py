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
    def has_path_sum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return None

        targetSum -= root.val
        if root.left is root.right:
            return targetSum == 0
        return self.has_path_sum(root.left, targetSum) or self.has_path_sum(root.right, targetSum)


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_has_path_sum(self):
        root = TreeNode.from_lst([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1])
        result = self.solution.has_path_sum(root, 22)
        self.assertTrue(result)
        

if __name__ == "__main__":
    unittest.main()
