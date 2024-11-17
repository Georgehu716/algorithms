package leetcode

import "testing"

func TestLongestOnes(t *testing.T) {
	testCases := []struct{
		nums []int
		k int
		ans int
	}{
		{[]int{1,1,1,0,0,0,1,1,1,1,0}, 2, 6},
		{[]int{0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1}, 3, 10},
		{[]int{0, 0, 0, 0, 0}, 2, 2},
		{[]int{}, 0, 0},
	}

	for _, tc := range testCases {
		result := longestOnes(tc.nums, tc.k)
		if result != tc.ans {
			t.Errorf("longestOnes(%v, %d) = %d; expected: %d", tc.nums, tc.k, result, tc.ans)
		}
	}
}
