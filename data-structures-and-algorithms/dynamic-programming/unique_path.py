"""
- https://medium.com/@al.eks/the-ultimate-guide-to-dynamic-programming-65865ef7ec5b

Leetcode #62 - Unique Paths

A robot is located at the top-left corner of an m * n grid. The robot can only
move either down or right at any point in time. The robot is trying to reach
the bottom-right corner of the grid. How many possible unique paths are there?
"""


class Solution:
    def unique_paths_recursive(self, m, n):
        """
        TIME: Exponential
        SPACE: O(max(m, n))
        """
        def helper(m, n):
            if m == 1 or n == 1:
                return 1

            return helper(m, n - 1) + helper(m - 1, n)

        return helper(m, n)

    def unique_paths_memorization(self, m, n):
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

        def helper(m, n):
            if dp[m][n]:
                return dp[m][n]
            elif m == 1 or n == 1:
                dp[m][n] = 1
                return dp[m][n]

            dp[m][n] = helper(m-1, n) + helper(m, n-1)
            return dp[m][n]
