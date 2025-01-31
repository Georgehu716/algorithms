import unittest
from typing import Optional
from bisect import bisect_left


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
    def closest_nodes(self, root: Optional[TreeNode], queries: list[int]) -> list[list[int]]:
        nums = []
        def dfs(node: Optional[TreeNode]) -> None:
            if node is None:
                return
            dfs(node.left)
            nums.append(node.val)
            dfs(node.right)
        dfs(root)

        n = len(nums)
        ans = []
        for q in queries:
            j = bisect_left(nums, q)
            mx = nums[j] if j < n else - 1
            if j == n or nums[j] != q:
                j -= 1
            mn = nums[j] if j >= 0 else -1
            ans.append([mn, mx])
        return ans


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_closest_nodes(self):
        root = TreeNode.from_lst([6, 2, 13, 1, 4, 9, 15, None, None, None, None, None, None, 14])
        result = self.solution.closest_nodes(root, [2, 5, 16])
        self.assertEqual(result, [[2, 2], [4, 6], [15, -1]])


if __name__ == "__main__":
    unittest.main()
