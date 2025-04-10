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
        """
        TIME: O(m * n)
        SPACE: O(m * n) [but limited to max call stack size and susceptible to overflow]
        """
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

        def helper(m, n):
            if dp[m][n]:
                return dp[m][n]
            elif m == 1 or n == 1:
                dp[m][n] = 1
                return dp[m][n]

            dp[m][n] = helper(m-1, n) + helper(m, n-1)
            return dp[m][n]

    def unique_paths_iteration_and_tabulation(self, m, n):
        """
        TIME: O(n * m)
        SPACE: O(n * m)
        """
        dp = [[1 for _ in range(n)] for _ in range(m)]

        for r in range(len(dp) - 2, -1, -1):
            for c in range(len(dp[r]) - 2, -1, -1):
                dp[r][c] = dp[r+1][c] + dp[r][c+1]

        return dp[0][0]

    def unique_paths_iteration_and_tabulation_with_space_optimized(self, m, n):
        """
        TIME: O(n * m)
        SPACE: O(n)
        """
        dp = [[1 for _ in range(n)] for _ in range(2)]

        for r in range(m - 2, -1, -1):
            for c in range(n - 2, -1, -1):
                dp[0][c] = dp[1][c] + dp[0][c+1]
            dp[1] = dp[0]
        return dp[0][0]
