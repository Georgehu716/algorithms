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
    def construct_from_pre_post(self, preorder: list[int], postorder: list[int]) -> Optional[TreeNode]:
        if not preorder:
            return None
        if len(preorder) == 1:
            return TreeNode(preorder[0])
        left_size = postorder.index(preorder[1]) + 1
        left = self.construct_from_pre_post(preorder[1: 1 + left_size], postorder[:left_size])
        right = self.construct_from_pre_post(preorder[1 + left_size:], postorder[left_size: -1])
        return TreeNode(preorder[0], left, right)


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_construct_from_pre_post(self):
        preorder = [1, 2, 4, 5, 3, 6, 7]
        postorder = [4, 5, 2, 6, 7, 3, 1]
        result = self.solution.construct_from_pre_post(preorder, postorder)
        self.assertEqual(result.to_list(), [1, 2, 3, 4, 5, 6, 7])


if __name__ == "__main__":
    unittest.main()
