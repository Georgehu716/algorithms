package leetcode

import "testing"

func TestSearch(t *testing.T) {
        testCases := []struct{
                nums []int
                target int
                ans int
        }{
                {[]int{4, 5, 6, 7, 0, 1, 2}, 0, 4},
                {[]int{4, 5, 6, 7, 0, 1, 2}, 3, -1},
                {[]int{1}, 0, -1},
        }

        for _, tc := range testCases {
                result := search(tc.nums, tc.target)
                if tc.ans != result {
                        t.Errorf("search(%v, %d) = %d; expected: %d", tc.nums, tc.target, result, tc.ans)
                }
        }
}
