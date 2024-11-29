package leetcode

import "testing"

func TestCountSubarrays(t *testing.T) {
	testCases := []struct{
		nums []int
		k int64
		ans int64
	}{
		{[]int{2, 1, 4, 3, 5}, 10, 6},
		{[]int{1, 1, 1}, 5, 5},
		{[]int{}, 0, 0},
	}

	for _, tc := range testCases {
		result := countSubarrays(tc.nums, tc.k)
		if result != tc.ans {
			t.Errorf("countSubarrays(%v, %d) = %d; expected: %d", tc.nums, tc.k, result, tc.ans)
		}
	}
}
