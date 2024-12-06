package leetcode

func find_min(nums []int) int {
        left, right := 0, len(nums) - 1
        for left <= right {
                mid := left + (right - left) / 2
                if nums[mid] > nums[len(nums) - 1] {
                        left = mid + 1
                } else {
                        right = mid - 1
                }
        }
        return left
}

func search(nums []int, target int) int {
        left, right := 0, len(nums) - 1
        if target <= nums[len(nums) - 1] {
                second_min := find_min(nums)
                left = second_min
        } else {
                second_min := find_min(nums)
                if second_min == 0 {
                        right = len(nums) - 1
                } else {
                        right = second_min + 1
                }
        }

        for left <= right {
                mid := left + (right - left) / 2
                if nums[mid] == target {
                        return mid
                } else if nums[mid] > target {
                        right = mid - 1
                } else {
                        left = mid + 1
                }
        }
        return -1
}
