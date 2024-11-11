package leetcode

import "testing"

func TestMinSubArrayLen(t *testing.T) {
	testCases := []struct {
		target int
		nums []int
		ans int
	}{
		{7, []int{2, 3, 1, 2, 4, 3}, 2},
		{4, []int{1, 4, 4}, 1},
		{11, []int{1, 1, 1, 1, 1, 1, 1, 1}, 0},
	}

	for _, tc := range testCases {
		result := minSubArrayLen(tc.target, tc.nums)
		if result != tc.ans {
			t.Errorf("minSubArrayLen(%d, %v) = %d; expected: %d", tc.target, tc.nums, result, tc.ans)
		}
	}
}
