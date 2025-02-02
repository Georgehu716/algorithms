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
    def max_sum_bst(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def dfs(node: Optional[TreeNode]) -> tuple:
            if node is None:
                return math.inf, -math.inf, 0
            l_min, l_max, l_sum = dfs(node.left)
            r_min, r_max, r_sum = dfs(node.right)
            x = node.val
            if x <= l_max or x >= r_min:
                return -math.inf, math.inf, 0
            s = l_sum + r_sum + x
            nonlocal ans
            ans = max(ans, s)
            return min(l_min, x), max(r_max, x), s

        dfs(root)
        return ans


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_max_sum_bst(self):
        root = TreeNode.from_lst([1, 4, 3, 2, 4, 2, 5, None, None, None, None, None, None, 4, 6])
        result = self.solution.max_sum_bst(root)
        self.assertEqual(result, 20)


if __name__ == "__main__":
    unittest.main()
