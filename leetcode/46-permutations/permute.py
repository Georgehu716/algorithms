import unittest


class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        n = len(nums)
        ans = []
        path = [0] * n
        on_path = [False] * n

        def dfs(i: int) -> None:
            if i == n:
                ans.append(path.copy())
                return
            for j, on in enumerate(on_path):
                if not on:
                    path[i] = nums[j]
                    on_path[j] = True
                    dfs(i + 1)
                    on_path[j] = False
        dfs(0)
        return ans


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_permute(self):
        result = self.solution.permute([1, 2, 3])
        self.assertEqual(sorted(result), sorted([[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]))


if __name__ == "__main__":
    unittest.main()
