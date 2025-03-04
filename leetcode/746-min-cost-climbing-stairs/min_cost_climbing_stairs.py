import unittest


class Solution:
    def min_cost_climbing_stairs(self, cost: list[int]) -> int:
        n = len(cost)
        f0 = f1 = 0
        for i in range(1, n):
            new_f = min(f1 + cost[i], f0 + cost[i - 1])
            f0 = f1
            f1 = new_f
        return f1


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_min_cost_climbing_stairs(self):
        result = self.solution.min_cost_climbing_stairs([10, 15, 20])
        self.assertEqual(result, 15)


if __name__ == "__main__":
    unittest.main()
