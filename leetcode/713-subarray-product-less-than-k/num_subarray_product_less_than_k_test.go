package leetcode

import "testing"

func TestNumSubarrayProductLessThanK(t *testing.T) {
	testCases := []struct{
		nums []int
		k int
		ans int
	}{
		{[]int{10, 5, 2, 6}, 100, 8},
		{[]int{1, 2, 3}, 0, 0},
	}

	for _, tc := range testCases {
		result := numSubarrayProductLessThanK(tc.nums, tc.k)
		if result != tc.ans {
			t.Errorf("numSubarrayProductLessThanK(%v, %d) = %d; expected: %d", tc.nums, tc.k, result, tc.ans)
		}
	}
}
