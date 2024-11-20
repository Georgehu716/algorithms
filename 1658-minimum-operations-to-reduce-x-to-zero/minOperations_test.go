package leetcode

import "testing"

func TestMinOperations(t *testing.T) {
	testCases := []struct{
		nums []int
		x int
		ans int
	}{
		{[]int{1, 1, 4, 2, 3}, 5, 2},
		{[]int{5, 6, 7, 8, 9}, 4, -1},
		{[]int{3, 2, 20, 1, 1, 3}, 10, 5},
	}

	for _, tc := range testCases {
		result := minOperations(tc.nums, tc.x)
		if result != tc.ans {
			t.Errorf("minOperations(%v, %d) = %d; expected: %d", tc.nums, tc.x, result, tc.ans)
		}
	}
}
