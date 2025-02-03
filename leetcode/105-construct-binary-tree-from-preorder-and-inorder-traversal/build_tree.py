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
    def build_tree(self, preorder: list[int], inorder: list[int]) -> Optional[TreeNode]:
        if not preorder:
            return None
        left_size = inorder.index(preorder[0])
        left = self.build_tree(preorder[1:1 + left_size], inorder[:left_size])
        right = self.build_tree(preorder[1+left_size:], inorder[1+left_size:])
        return TreeNode(preorder[0], left, right)


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_build_tree(self):
        preorder = [3, 9, 20, 15, 7]
        inorder = [9, 3, 15, 20, 7]
        result = self.solution.build_tree(preorder, inorder)
        self.assertEqual(result.to_list(), [3, 9, 20, None, None, 15, 7])


if __name__ == "__main__":
    unittest.main()
