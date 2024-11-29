package leetcode

import "testing"

func TestTrap(t *testing.T) {
	testCases := []struct {
		height []int
		ans int
	}{
		{[]int{0,1,0,2,1,0,1,3,2,1,2,1}, 6},
		{[]int{4,2,0,3,2,5}, 9},
		{[]int{0, 0, 0, 0, 0}, 0},
	}

	for _, tc := range testCases {
		result := trap(tc.height)
		if result != tc.ans {
			t.Errorf("trap(%v) = %d; expected: %d", tc.height, result, tc.ans)
		}
	}
}
