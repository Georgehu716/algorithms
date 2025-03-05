import unittest


class Solution:
    def combination_sum_4(self, nums: list[int], target: int) -> int:
        f = [1] + [0] * target
        for i in range(1, target + 1):
            f[i] = sum(f[i - x] for x in nums if x <= i)
        return f[target]


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_combination_sum_4(self):
        result = self.solution.combination_sum_4([1, 2, 3], 4)
        self.assertEqual(result, 7)


if __name__ == "__main__":
    unittest.main()
