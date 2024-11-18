package leetcode

import "slices"

func countSubarrays(nums []int, k int) (ans int64) {
	maxNum := slices.Max(nums)
	left, cnt := 0, 0
	for _, x := range nums {
		if x == maxNum {
			cnt++
		}
		for cnt >= k {
			if nums[left] == maxNum {
				cnt--
			}
			left++
		}
		ans += int64(left)
	}
	return
}
