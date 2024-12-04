package leetcode

func findPeakElement(nums []int) int {
        left, right := -1, len(nums) - 1
        for left + 1 < right {
                mid := left + (right - left) / 2
                if nums[mid] > nums[mid + 1] {
                        right = mid
                } else {
                        left = mid
                }
        }
        return right
}
