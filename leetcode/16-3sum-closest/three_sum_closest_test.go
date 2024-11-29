package leetcode

import "testing"

func TestThreeSumClosest(t *testing.T) {
	testCases := []struct {
		nums []int
		target int
		ans int
	}{
		{[]int{-1, 2, 1, -4}, 1, 2},
		{[]int{0, 0, 0}, 1, 0},
		{[]int{1, 1, 1, 0}, 100, 3},
		{[]int{-1000, -1000, -1000}, 10000, -3000},
	}
	for _, tc := range testCases {
		result := threeSumClosest(tc.nums, tc.target)
		if result != tc.ans {
			t.Errorf("threeSumClosest(%v, %d) = %d; expected: %d", tc.nums, tc.target, result, tc.ans)
		}
	}
}
