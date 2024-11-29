package leetcode

import "testing"

func TestMinWindow(t *testing.T) {
	testCases := []struct{
		s, t, ans string
	}{
		{"ADOBECODEBANC", "ABC", "BANC"},
		{"a", "a", "a"},
		{"a", "aa", ""},
	}

	for _, tc := range testCases {
		result := minWindow(tc.s, tc.t)
		if result != tc.ans {
			t.Errorf("minWindow(%v, %v) = %v; expected: %v", tc.s, tc.t, result, tc.ans)
		}
	}
}
