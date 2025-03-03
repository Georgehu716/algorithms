import unittest


class Solution:
    def climb_stairs(self, n: int) -> int:
        f0 = f1 = 1
        for _ in range(2, n + 1):
            new_f = f0 + f1
            f0 = f1
            f1 = new_f
        return f1


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_climb_stairs(self):
        result = self.solution.climb_stairs(3)
        self.assertEqual(result, 3)


if __name__ == "__main__":
    unittest.main()
