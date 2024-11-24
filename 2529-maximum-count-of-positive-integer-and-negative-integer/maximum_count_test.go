package leetcode

import "testing"

func TestMaximumCount(t *testing.T) {
	testCases := []struct{
		nums []int
		ans int
	}{
		{[]int{-2, -1, -1, 1, 2, 3}, 3},
		{[]int{-3, -2, -1, 0, 0, 1, 2}, 3},
		{[]int{5, 20, 66, 1314}, 4},
	}

	for _, tc := range testCases {
		result := maximumCount(tc.nums)
		if result != tc.ans {
			t.Errorf("maximumCount(%v) = %d; expected: %d", tc.nums, result, tc.ans)
		}
	}
}
