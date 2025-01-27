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
    def merge_trees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if root1 is None:
            return root2
        if root2 is None:
            return root1
        return TreeNode(root1.val + root2.val,
            self.merge_trees(root1.left, root2.left),
            self.merge_trees(root1.right, root2.right))


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_merge_trees(self):
        root1 = TreeNode.from_lst([1, 3, 2, 5])
        root2 = TreeNode.from_lst([2, 1, 3, None, 4, None, 7])
        result = self.solution.merge_trees(root1, root2)
        self.assertEqual(result.to_list(), [3, 4, 5, 5, 4, None, 7])


if __name__ == "__main__":
    unittest.main()
