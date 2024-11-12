package leetcode

import "testing"

func TestLengthOfLongestSubstring(t *testing.T) {
	testCases := []struct{
		s string
		ans int
	}{
		{"abcabcbb", 3},
		{"bbbbb", 1},
		{"pwwkew", 3},
		{"", 0},
	}

	for _, tc := range testCases {
		result := lengthOfLongestSubstring(tc.s)
		if result != tc.ans {
			t.Errorf("lengthOfLongestSubstring(%q) = %d; expected: %d", tc.s, result, tc.ans)
		}
	}
}
