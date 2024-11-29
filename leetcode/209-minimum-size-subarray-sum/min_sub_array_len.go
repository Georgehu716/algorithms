package leetcode

func minSubArrayLen(target int, nums []int) int {
	n := len(nums)
	ans, sum, left := n + 1, 0, 0
	for right, x := range nums {
		sum += x
		for sum >= target {
			ans = min(ans, right - left + 1)
			sum -= nums[left]
			left++
		}
	}
	if ans <= n {
		return ans
	}
	return 0
}
