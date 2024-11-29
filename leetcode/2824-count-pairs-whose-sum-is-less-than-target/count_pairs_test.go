package leetcode

import "testing"

func TestCountPairs(t *testing.T) {
	testCases := []struct {
		nums     []int
		target   int
		expected int
	}{
		{[]int{-1, 1, 2, 3, 1}, 2, 3},
		{[]int{-6, 2, 5, -2, -7, -1, 3}, -2, 10},
		{[]int{}, 0, 0},                  // Edge case: empty array
		{[]int{1, 2, 3, 4, 5}, 0, 0},     // Edge case: no pairs less than target
		{[]int{-3, -2, -1, 0, 1}, 3, 10}, // Edge case: all pairs valid
	}

	for _, tc := range testCases {
		result := countPairs(tc.nums, tc.target)
		if result != tc.expected {
			t.Errorf("countPairs(%v, %d) = %d; expected: %d", tc.nums, tc.target, result, tc.expected)
		}
	}
}
