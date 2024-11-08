package leetcode

import "slices"

func triangleNumber(nums []int) (ans int) {
	slices.Sort(nums)
	for k := 2; k < len(nums); k++ {
		i, j := 0, k - 1
		for i < j {
			if nums[i] + nums[j] > nums[k] {
				ans += j - i
				j--
			} else {
				i++
			}
		}
	}
	return
}
