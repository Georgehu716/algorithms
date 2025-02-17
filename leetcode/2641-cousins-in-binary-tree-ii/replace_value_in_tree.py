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
            result.append(node.val if node else None)
            if node:
                queue.append(node.left)
                queue.append(node.right)
        while result and result[-1] is None:
            result.pop()
        return result


class Solution:
    def replace_value_in_tree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        root.val = 0
        q = [root]
        while q:
            tmp = q
            q = []

            next_level_sum = 0
            for node in tmp:
                if node.left:
                    q.append(node.left)
                    next_level_sum += node.left.val
                if node.right:
                    q.append(node.right)
                    next_level_sum += node.right.val
            for node in tmp:
                children_sum = (node.left.val if node.left else 0) + \
                                (node.right.val if node.right else 0)
                if node.left:
                    node.left.val = next_level_sum - children_sum
                if node.right:
                    node.right.val = next_level_sum - children_sum
        return root


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_replace_value_in_tree(self):
        root = TreeNode.from_lst([5, 4, 9, 1, 10, None, 7])
        expected = [0, 0, 0, 7, 7, None, 11]
        result = self.solution.replace_value_in_tree(root)
        self.assertEqual(result.to_list(), expected)


if __name__ == "__main__":
    unittest.main()
