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

    def to_list(self):
        result = []
        queue = [self]
        while queue:
            node = queue.pop(0)
            if node:
                result.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
            else:
                result.append(None)
        while result and result[-1] is None:
            result.pop()
        return result


class Solution:
    def sufficient_subset(self, root: Optional[TreeNode], limit: int) -> Optional[TreeNode]:
        limit -= root.val
        if root.left is root.right:
            return None if limit > 0 else root
        if root.left:
            root.left = self.sufficient_subset(root.left, limit)
        if root.right:
            root.right = self.sufficient_subset(root.right, limit)
        return root if root.left or root.right else None


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_sufficient_subset(self):
        root = TreeNode.from_lst([1, 2, 3, 4, -99, -99, 7, 8, 9, -99, -99, 12, 13, -99, 14])
        result = self.solution.sufficient_subset(root, 1)
        self.assertEqual(result.to_list(), [1, 2, 3, 4, None, None, 7, 8, 9, None, 14])


if __name__ == "__main__":
    unittest.main()
