package leetcode

import (
	"testing"
	"reflect"
)

func TestSearchRange(t *testing.T) {
	testCases := []struct{
		nums []int
		target int
		ans []int
	}{
		{[]int{5, 7, 7, 8, 8, 10}, 8, []int{3, 4}},
		{[]int{5, 7, 7, 8, 8, 10}, 6, []int{-1, -1}},
		{[]int{}, 0, []int{-1, -1}},
	}

	for _, tc := range testCases {
		result := searchRange(tc.nums, tc.target)
		if !reflect.DeepEqual(result, tc.ans) {
			t.Errorf("searchRange(%v, %d) = %v; expected: %v", tc.nums, tc.target, result, tc.ans)
		}
	}
}
