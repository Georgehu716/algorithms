import unittest


class Solution:
    def generate_parenthesis(self, n: int) -> list[str]:
        ans = []

        def backtrack(S, left, right):
            if len(S) == 2 * n:
                ans.append(''.join(S))
                return
            if left < n:
                S.append("(")
                backtrack(S, left + 1, right)
                S.pop()
            if right < left:
                S.append(")")
                backtrack(S, left, right + 1)
                S.pop()
        backtrack([], 0, 0)
        return ans


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_generate_parenthesis(self):
        result = self.solution.generate_parenthesis(3)
        self.assertEqual(sorted(result), sorted(["((()))","(()())","(())()","()(())","()()()"]))


if __name__ == "__main__":
    unittest.main()
