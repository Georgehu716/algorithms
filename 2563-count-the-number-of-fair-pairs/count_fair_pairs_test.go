package leetcode

import "testing"

func TestCountFairPairs(t *testing.T) {
	testCases := []struct{
		nums []int
		lower int
		upper int
		ans int64
	}{
		{[]int{0, 1, 7, 4, 4, 5}, 3, 6, 6},
		{[]int{1, 7, 9, 2, 5}, 11, 11, 1},
	}

	for _, tc := range testCases {
		result := countFairPairs(tc.nums, tc.lower, tc.upper)
		if result != tc.ans {
			t.Errorf("countFairPairs(%v, %d, %d) = %d; expected: %d", tc.nums, tc.lower, tc.upper, result, tc.ans)
		}
	}
}
