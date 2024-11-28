package leetcode

import "testing"

func TestHIndex(t *testing.T) {
	testCases := []struct{
		citations []int
		ans int
	}{
		{[]int{0, 1, 3, 5, 6}, 3},
		{[]int{1, 2, 100}, 2},
		{[]int{1}, 1},
		{[]int{100}, 1},
	}

	for _, tc := range testCases {
		result := hIndex(tc.citations)
		if result != tc.ans {
			t.Errorf("hIndex(%v) = %d; expected: %d", tc.citations, result, tc.ans)
		}
	}
}
