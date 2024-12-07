package leetcode

import (
	"testing"
	"reflect"
)

func TestFindPeakGrid(t *testing.T) {
	testCases := []struct{
		mat [][]int
		ans []int
	}{
		{[][]int{{1, 4}, {3, 2}}, []int{0, 1}},
		{[][]int{{10, 20, 15}, {21, 30, 14}, {7, 16, 32}}, []int{1, 1}},
	}

	for _, tc := range testCases {
		result := findPeakGrid(tc.mat)
		if !reflect.DeepEqual(result, tc.ans) {
			t.Errorf("findPeakGrid(%v) = %v; expected: %v", tc.mat, result, tc.ans)
		}
	}
}
