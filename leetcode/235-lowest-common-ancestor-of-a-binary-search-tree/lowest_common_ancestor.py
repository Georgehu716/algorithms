import unittest


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    @staticmethod
    def from_lst(lst):
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

    def find(self, val):
        if self.val == val:
            return self
        elif self.val > val:
            return self.left.find(val)
        else:
            return self.right.find(val)
        return None


class Solution:
    def lowest_common_ancestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        x = root.val
        if p.val > x and q.val > x:
            return self.lowest_common_ancestor(root.right, p, q)
        if p.val < x and q.val < x:
            return self.lowest_common_ancestor(root.left, p, q)
        return root


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_lowest_common_ancestor(self):
        root = TreeNode.from_lst([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5])
        p = root.find(2)
        q = root.find(8)
        result = self.solution.lowest_common_ancestor(root, p, q)
        self.assertEqual(result.val, 6)


if __name__ == "__main__":
    unittest.main()
