package leetcode

import "testing"

func TestMinimumTime(t *testing.T) {
	testCases := []struct{
		time []int
		totalTrips int
		ans int64
	}{
		{[]int{1, 2, 3}, 5, 3},
		{[]int{2}, 1, 2},
	}

	for _, tc := range testCases {
		result := minimumTime(tc.time, tc.totalTrips)
		if result != tc.ans {
			t.Errorf("minimumTime(%v, %d) = %d; expected: %d", tc.time, tc.totalTrips, result, tc.ans)
		}
	}
}
