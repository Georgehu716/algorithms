package leetcode

func numSubarrayProductLessThanK(nums []int, k int) (ans int) {
	left, prod := 0, 1
	for right, v := range nums {
		prod *= v
		for prod >= k && left <= right {
			prod /= nums[left]
			left++
		}
		ans += (right - left + 1)
	}
	return
}
