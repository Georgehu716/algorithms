import unittest


class Solution:
    def combination_sum(self, candidates: list[int], target: int) -> list[list[int]]:
        ans = []
        path = []

        def dfs(i: int, left: int) -> None:
            if left == 0:
                ans.append(path.copy())
                return
            if i == len(candidates) or left < 0:
                return
            dfs(i + 1, left)
            path.append(candidates[i])
            dfs(i, left - candidates[i])
            path.pop()
        dfs(0, target)
        return ans


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_combination_sum(self):
        result = self.solution.combination_sum([2, 3, 6, 7], 7)
        self.assertEqual(sorted(result), sorted([[2, 2, 3], [7]]))


if __name__ == "__main__":
    unittest.main()
