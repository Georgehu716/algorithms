package leetcode

import "testing"

func TestFindPeakElement(t *testing.T) {
        testCases := []struct{
                nums []int
                ans []int
        }{
                {[]int{1, 2, 3, 1}, []int{2}},
                {[]int{1, 2, 1, 3, 5, 6, 4}, []int{1, 5}},
        }

        for _, tc := range testCases {
                result := findPeakElement(tc.nums)

                isValid := false
                for _, v := range tc.ans {
                        if result == v {
                                isValid = true
                                break
                        }
                }

                if !isValid {
                        t.Errorf("findPeakElement(%v) = %d; expected one of %v", tc.nums, result, tc.ans)
                }
        }
}
