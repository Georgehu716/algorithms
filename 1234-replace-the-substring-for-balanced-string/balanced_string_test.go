package leetcode

import "testing"

func TestBalancedString(t *testing.T) {
	testCases := []struct{
		s string
		ans int
	}{
		{"QERW", 0},
		{"QQWE", 1},
		{"QQQE", 2},
		{"QQQQ", 3},
	}

	for _, tc := range testCases {
		result := balancedString(tc.s)
		if result != tc.ans {
			t.Errorf("balancedString(%v) = %d; expected: %d", tc.s, result, tc.ans)
		}
	}
}
