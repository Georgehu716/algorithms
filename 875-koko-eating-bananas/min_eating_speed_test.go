package leetcode

import "testing"

func TestMinEatingSpeed(t *testing.T) {
	testCases := []struct{
		piles []int
		h int
		ans int
	}{
		{[]int{3, 6, 7, 11}, 8, 4},
		{[]int{30, 11, 23, 4, 20}, 5, 30},
		{[]int{30, 11, 23, 4, 20}, 6, 23},
	}

	for _, tc := range testCases {
		result := minEatingSpeed(tc.piles, tc.h)
		if result != tc.ans {
			t.Errorf("minEatingSpeed(%v, %d) = %d; expected: %d", tc.piles, tc.h, result, tc.ans)
		}
	}
}
