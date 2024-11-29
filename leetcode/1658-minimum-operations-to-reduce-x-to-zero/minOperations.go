package leetcode

func minOperations(nums []int, x int) int {
	total := 0
	for _, v := range nums {
		total += v
	}

	n := len(nums)
	ans := -1
	left, s := 0, 0
	for right, v := range nums {
		s += v
		for s > (total - x) && left <= right {
			s -= nums[left]
			left++
		}
		if s == (total - x) {
			ans = max(ans, right - left + 1)
		}
	}
	if ans < 0 {
		return -1
	}
	return n - ans
}
