import unittest


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

    def find(self, val):
        if self.val == val:
            return self
        if self.left:
            found = self.left.find(val)
            if found:
                return found
        if self.right:
            found = self.right.find(val)
            if found:
                return found
        return None


class Solution:
    def lowest_common_ancestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root in (None, p, q):
            return root
        left = self.lowest_common_ancestor(root.left, p, q)
        right = self.lowest_common_ancestor(root.right, p, q)
        if left and right:
            return root
        return left or right


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_lowest_common_ancestor(self):
        root = TreeNode.from_lst([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])
        p = root.find(5)
        q = root.find(1)
        result = self.solution.lowest_common_ancestor(root, p, q)
        self.assertEqual(result.val, 3)


if __name__ == "__main__":
    unittest.main()
