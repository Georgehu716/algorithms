import unittest


class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        ans = []
        path = []
        n = len(nums)

        def dfs(i: int) -> None:
            if i == n:
                ans.append(path.copy())
                return
            dfs(i + 1)
            path.append(nums[i])
            dfs(i + 1)
            path.pop()
        dfs(0)
        return ans


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_subsets(self):
        nums = [1, 2, 3]
        result = self.solution.subsets(nums)
        self.assertEqual(sorted(result), sorted([[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]))


if __name__ == "__main__":
    unittest.main()
