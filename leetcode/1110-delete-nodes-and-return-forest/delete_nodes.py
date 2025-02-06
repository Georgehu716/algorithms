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
    def del_nodes(self, root: Optional[TreeNode], to_delete: list[int]) -> list[TreeNode]:
        ans = []
        s = set(to_delete)
        def dfs(node: Optional[TreeNode]) -> Optional[TreeNode]:
            if node is None:
                return None
            node.left = dfs(node.left)
            node.right = dfs(node.right)
            if node.val not in s:
                return node
            if node.left:
                ans.append(node.left)
            if node.right:
                ans.append(node.right)
            return None
        if dfs(root):
            ans.append(root)
        return ans


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def test_del_nodes(self):
        root = TreeNode.from_lst([1, 2, 3, 4, 5, 6, 7])
        to_delete = [3, 5]
        result = self.solution.del_nodes(root, to_delete)
        result_lists = [tree.to_list() for tree in result]
        self.assertEqual(sorted(result_lists), sorted([[1, 2, None, 4], [6], [7]]))


if __name__ == "__main__":
    unittest.main()
