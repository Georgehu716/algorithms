package leetcode

func findMin(nums []int) int {
	left, right := -1, len(nums) - 1
	for left + 1 < right {
		mid := left + (right - left) / 2
		if nums[mid] < nums[right] {
			right = mid
		} else if nums[mid] > nums[right] {
			left = mid
		} else {
			right--
		}
	}
	return nums[right]
}
