package leetcode

import (
	"testing"
	"reflect"
)

func TestFourSum(t *testing.T) {
	testCases := []struct {
		nums []int
		target int
		ans [][]int
	}{
		{[]int{1, 0, -1, 0, -2, 2}, 0, [][]int{{-2, -1, 1, 2}, {-2, 0, 0, 2}, {-1, 0, 0, 1}}},
		{[]int{2, 2, 2, 2, 2}, 8, [][]int{{2, 2, 2, 2}}},
		{[]int{0, 0, 0, 0}, 0, [][]int{{0, 0, 0, 0}}},
		{[]int{1, 2, 3, 4}, 50, [][]int{}},
	}

	for _, tc := range testCases {
		result := fourSum(tc.nums, tc.target)
		if len(result) == 0 && len(tc.ans) == 0 {
			continue
		}

		if !reflect.DeepEqual(result, tc.ans) {
			t.Errorf("fourSum(%v, %d) = %v; expected: %v", tc.nums, tc.target, result, tc.ans)
		}
	}
}
