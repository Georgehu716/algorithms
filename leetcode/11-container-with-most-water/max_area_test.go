package leetcode

import "testing"

func TestMaxArea(t *testing.T) {
	testCases := []struct {
		height []int
		ans int
	}{
		{[]int{1,8,6,2,5,4,8,3,7}, 49},
		{[]int{1, 1}, 1},
		{[]int{0, 0}, 0},
	}

	for _, tc := range testCases {
		result := maxArea(tc.height)
		if result != tc.ans {
			t.Errorf("maxArea(%v) = %d; expected: %d", tc.height, result, tc.ans)
		}
	}
}
