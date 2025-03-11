import unittest
from math import inf


class Solution:
    def coin_change(self, coins: list[int], amount: int) -> int:
        f = [0] + [inf] * amount
        for x in coins:
            for c in range(x, amount + 1):
                f[c] = min(f[c], f[c - x] + 1)
        ans = f[amount]
        return ans if ans < inf else -1


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_coin_change(self):
        result = self.solution.coin_change([1, 2, 5], 11)
        self.assertEqual(result, 3)


if __name__ == "__main__":
    unittest.main()
