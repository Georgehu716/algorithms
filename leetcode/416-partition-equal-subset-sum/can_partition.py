import unittest
from functools import cache


class Solution:
    def can_partition(self, nums: list[int]) -> bool:
        @cache
        def dfs(i: int, c: int) -> bool:
            if i < 0:
                return c == 0
            return c >= nums[i] and dfs(i - 1, c - nums[i]) or dfs(i - 1, c)
        s = sum(nums)
        return s % 2 == 0 and dfs(len(nums) - 1, s // 2)


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_can_partition(self):
        result = self.solution.can_partition([1, 5, 11, 5])
        self.assertTrue(result)


if __name__ == "__main__":
    unittest.main()
