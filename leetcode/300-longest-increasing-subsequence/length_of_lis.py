import unittest
from functools import cache


class Solution:
    def length_of_lis(self, nums: list[int]) -> int:
        @cache
        def dfs(i: int) -> int:
            res = 0
            for j in range(i):
                if nums[j] < nums[i]:
                    res = max(res, dfs(j))
            return res + 1
        return max(dfs(i) for i in range(len(nums)))


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_length_of_lis(self):
        result = self.solution.length_of_lis([10, 9, 2, 5, 3, 7, 101, 18])
        self.assertEqual(result, 4)


if __name__ == "__main__":
    unittest.main()
