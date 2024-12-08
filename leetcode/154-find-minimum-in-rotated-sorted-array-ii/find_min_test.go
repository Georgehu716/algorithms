package leetcode

import "testing"

func TestFindMin(t *testing.T) {
	testCases := []struct{
		nums []int
		ans int
	}{
		{[]int{1, 3, 5}, 1},
		{[]int{2, 2, 2, 0, 1}, 0},
	}

	for _, tc := range testCases {
		result := findMin(tc.nums)
		if result != tc.ans {
			t.Errorf("findMin(%v) = %d; expected: %d", tc.nums, result, tc.ans)
		}
	}
}
