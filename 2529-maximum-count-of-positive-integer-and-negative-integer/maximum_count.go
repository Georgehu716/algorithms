package leetcode

func lowerBound(nums []int, target int) int {
	left, right := 0, len(nums) - 1
	for left <= right {
		mid := left + (right - left) / 2
		if nums[mid] >= target {
			right = mid - 1
		} else {
			left = mid + 1
		}
	}
	return left
}

func maximumCount(nums []int) int {
	neg := lowerBound(nums, 0)
	pos := len(nums) - lowerBound(nums, 1)
	return max(neg, pos)
}
