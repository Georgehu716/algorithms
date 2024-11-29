package leetcode

import "testing"

func TestLongestSemiRepetitiveSubstring(t *testing.T) {
	testCases := []struct{
		s string
		ans int
	}{
		{"52233", 4},
		{"5494", 4},
		{"1111111", 2},
		{"1101234883", 9},
		{"122234", 4},
		{"0", 1},
	}

	for _, tc := range testCases {
		result := longestSemiRepetitiveSubstring(tc.s)
		if result != tc.ans {
			t.Errorf("longestSemiRepetitiveSubstring(%q) = %d; expected: %d", tc.s, result, tc.ans)
		}
	}
}
