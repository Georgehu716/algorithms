package leetcode

import "testing"

func TestTriangleNumber(t *testing.T) {
	testCases := []struct {
		nums []int
		ans int
	}{
		{[]int{2, 2, 3, 4}, 3},
		{[]int{4, 2, 3, 4}, 4},
		{[]int{0, 0, 0, 0}, 0},
		{[]int{1, 1, 1}, 1},
	}

	for _, tc := range testCases {
		result := triangleNumber(tc.nums)
		if result != tc.ans {
			t.Errorf("triangleNumber(%v) = %d, expected: %d", tc.nums, result, tc.ans)
		}
	}
}
