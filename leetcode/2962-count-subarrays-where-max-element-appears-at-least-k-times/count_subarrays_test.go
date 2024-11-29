package leetcode

import "testing"

func TestCountSubarrays(t *testing.T) {
	testCases := []struct{
		nums []int
		k int
		ans int64
	}{
		{[]int{1, 3, 2, 3, 3}, 2, 6},
		{[]int{1, 4, 2, 1}, 3, 0},
	}

	for _, tc := range testCases {
		result := countSubarrays(tc.nums, tc.k)
		if result != tc.ans {
			t.Errorf("countSubarrays(%v, %d) = %d; expected: %d", tc.nums, tc.k, result, tc.ans)
		}
	}
}
