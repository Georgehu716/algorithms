package leetcode

import "testing"

func TestMaxSubarrayLength(t *testing.T) {
	testCases := []struct{
		nums []int
		k int
		ans int
	}{
		{[]int{1, 2, 3, 1, 2, 3, 1, 2}, 2, 6},
		{[]int{1, 2, 1, 2, 1, 2, 1, 2}, 1, 2},
		{[]int{5, 5, 5, 5, 5, 5, 5}, 4, 4},
		{[]int{}, 0, 0},
	}

	for _, tc := range testCases {
		result := maxSubarrayLength(tc.nums, tc.k)
		if result != tc.ans {
			t.Errorf("maxSubarrayLength(%v, %d) = %d; expected: %d", tc.nums, tc.k, result, tc.ans)
		}
	}
}
