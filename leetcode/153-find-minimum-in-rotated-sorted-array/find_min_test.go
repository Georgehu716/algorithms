package leetcode

import "testing"

func TestFindMin(t *testing.T) {
        testCases := []struct{
                nums []int
                ans int
        }{
                {[]int{3, 4, 5, 1, 2}, 1},
                {[]int{4, 5, 6, 7, 0, 1, 2}, 0},
                {[]int{11, 13, 15, 17}, 11},
        }

        for _, tc := range testCases {
                result := findMin(tc.nums)
                if result != tc.ans {
                        t.Errorf("findMin(%v) = %d; expected: %d", tc.nums, result, tc.ans)
                }
        }
}
