"""
121. Best Time to Buy and Sell Stock

You are given an array `prices` where `prices[i]` is the price of a given stock on the `i^{th}` day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return `0`.
"""


import unittest


class Solution:
    def max_profit(self, prices: list[int]) -> int:
        ans = 0
        min_price = prices[0]
        for p in prices:
            ans = max(ans, p - min_price)
            min_price = min(min_price, p)
        return ans


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_max_profit(self):
        result = self.solution.max_profit([7, 1, 5, 3, 6, 4])
        self.assertEqual(result, 5)


if __name__ == "__main__":
    unittest.main()
