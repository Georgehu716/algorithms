package leetcode

import "testing"

func TestMinimizeArrayValue(t *testing.T) {
	testCases := []struct{
		nums []int
		ans int
	}{
		{[]int{3, 7, 1, 6}, 5},
		{[]int{10, 1}, 10},
	}

	for _, tc := range testCases {
		result := minimizeArrayValue(tc.nums)
		if result != tc.ans {
			t.Errorf("minimizeArrayValue(%v) = %d; expected: %d", tc.nums, result, tc.ans)
		}
	}
}
