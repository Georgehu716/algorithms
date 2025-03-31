"""
516. Longest Palindromic Subsequence

Given a string `s`, find the longest palindromic subsequence's length in `s`.

A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.
"""


import unittest


class Solution:
    def longest_palindrome_subseq(self, s: str) -> int:
        n = len(s)
        f = [[0] * n for _ in range(n)]
        for i in range(n-1, -1, -1):
            f[i][i] = 1
            for j in range(i + 1, n):
                if s[i] == s[j]:
                    f[i][j] = f[i + 1][j - 1] + 2
                else:
                    f[i][j] = max(f[i + 1][j], f[i][j - 1])

        return f[0][-1]


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_longest_palindrome_subseq(self):
        result = self.solution.longest_palindrome_subseq("bbbab")
        self.assertEqual(result, 4)


if __name__ == "__main__":
    unittest.main()
