"""
122. Best Time to Buy and Sell Stock II

You are given an integer array `prices` where `prices[i]` is the price of a given stock on the `i^{th}` day.

On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. However you can buy it then immediately sell it on the same day.

Find and return the maximum profit you can achieve.
"""


import unittest


class Solution:
    def max_profit(self, prices: list[int]) -> int:
        ans = 0
        n = len(prices)
        for i in range(n):
            if i < n - 1 and prices[i + 1] > prices[i]:
                ans += (prices[i + 1] - prices[i])
        return ans


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_max_profit(self):
        result = self.solution.max_profit([7, 1, 5, 3, 6, 4])
        self.assertEqual(result, 7)


if __name__ == "__main__":
    unittest.main()
