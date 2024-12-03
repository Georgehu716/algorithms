package leetcode

import "testing"

func TestMaximumTastiness(t *testing.T) {
	testCases := []struct{
		price []int
		k int
		ans int
	}{
		{[]int{13, 5, 1, 8, 21, 2}, 3, 8},
		{[]int{1, 3, 1}, 2, 2},
		{[]int{7, 7, 7, 7}, 2, 0},
	}

	for _, tc := range testCases {
		result := maximumTastiness(tc.price, tc.k)
		if result != tc.ans {
			t.Errorf("maximumTastiness(%v, %d) = %d; expected: %d", tc.price, tc.k, result, tc.ans)
		}
	}
}
