import unittest


class Solution:
    def count_good_strings(self, low: int, high: int, zero: int, one: int) -> int:
        MOD = 1_000_000_007
        f = [1] + [0] * high
        for i in range(1, high + 1):
            if i >= zero:
                f[i] = f[i - zero]
            if i >= one:
                f[i] = (f[i] + f[i - one]) % MOD
        return sum(f[low:]) % MOD


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_count_good_strings(self):
        result = self.solution.count_good_strings(3, 3, 1, 1)
        self.assertEqual(result, 8)


if __name__ == "__main__":
    unittest.main()
