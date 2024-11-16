package leetcode

import "testing"

func TestMaximumBeauty(t *testing.T) {
	testCases := []struct{
		nums []int
		k int
		ans int
	}{
		{[]int{4, 6, 1, 2}, 2, 3},
		{[]int{1, 1, 1, 1}, 10, 4},
		{[]int{}, 0, 0},
	}

	for _, tc := range testCases {
		result := maximumBeauty(tc.nums, tc.k)
		if result != tc.ans {
			t.Errorf("maximumBeauty(%v, %d) = %d; expected: %d", tc.nums, tc.k, result, tc.ans)
		}
	}
}
