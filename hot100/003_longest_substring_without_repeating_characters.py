import unittest


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        left, cur_len, max_len = 0, 0, 0
        lookup = set()
        
        for i in range(len(s)):
            cur_len += 1
            while s[i] in lookup:
                lookup.remove(s[left])
                left += 1
                cur_len -= 1
            if cur_len > max_len:
                max_len = cur_len
            lookup.add(s[i])
        return max_len


class TestSolution(unittest.TestCase):
    
    def test_lengthOfLongestSubstring(self):
        self.assertEqual(Solution().lengthOfLongestSubstring("abcabcbb"), 3)
        self.assertEqual(Solution().lengthOfLongestSubstring("bbbbb"), 1)


if __name__ == '__main__':
    unittest.main()
