import unittest


class Solution:
    def partition(self, s: str) -> list[list[str]]:
        ans = []
        n = len(s)
        path = []

        def dfs(i: int) -> None:
            if i == n:
                ans.append(path.copy())
                return
            for j in range(i, n):
                t = s[i: j + 1]
                if t == t[::-1]:
                    path.append(t)
                    dfs(j + 1)
                    path.pop()
        dfs(0)
        return ans


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_partition(self):
        s = "aab"
        result = self.solution.partition(s)
        self.assertEqual(sorted(result), sorted([["a", "a", "b"], ["aa", "b"]]))


if __name__ == "__main__":
    unittest.main()
