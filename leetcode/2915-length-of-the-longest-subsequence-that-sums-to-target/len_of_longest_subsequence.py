import unittest
from math import inf


class Solution:
    def length_of_longest_subsequence(self, nums: list[int], target: int) -> int:
        f = [0] + [-inf] * target
        s = 0
        for x in nums:
            s = min(s + x, target)
            for j in range(s, x - 1, -1):
                f[j] = max(f[j], f[j - x] + 1)
        return f[-1] if f[-1] > 0 else -1


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_length_of_longest_subsequence(self):
        result = self.solution.length_of_longest_subsequence([1, 2, 3, 4, 5], 9)
        self.assertEqual(result, 3)


if __name__ == "__main__":
    unittest.main()
