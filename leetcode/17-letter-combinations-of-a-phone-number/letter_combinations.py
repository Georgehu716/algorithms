import unittest


class Solution:
    def letter_combinations(self, digits: str) -> list[str]:
        MAPPING = "", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"
        n = len(digits)
        if n == 0:
            return []
        ans = []
        path = [''] * n
        def dfs(i: int) -> None:
            if i == n:
                ans.append(''.join(path))
                return
            nonlocal MAPPING
            for c in MAPPING[int(digits[i])]:
                path[i] = c
                dfs(i + 1)
        dfs(0)
        return ans


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_letter_combinations(self):
        digits = "23"
        result = self.solution.letter_combinations(digits)
        self.assertEqual(result, ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"])


if __name__ == "__main__":
    unittest.main()
