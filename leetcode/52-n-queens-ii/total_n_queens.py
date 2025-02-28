import unittest


class Solution:
    def total_n_queens(self, n: int) -> int:
        ans = []
        path = [-1] * n

        def dfs(i: int) -> None:
            if i == n:
                ans.append(path.copy())
                return
            flag = True
            for j in range(n):
                for x in range(i):
                    if (path[x] == j) or (path[x] == j - i + x) or (path[x] == j + i - x):
                        flag = False
                if flag:
                    path[i] = j
                    dfs(i + 1)
                else:
                    flag = True
        dfs(0)
        return len(ans)


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_total_n_queens(self):
        result = self.solution.total_n_queens(4)
        self.assertEqual(result, 2)


if __name__ == "__main__":
    unittest.main()
