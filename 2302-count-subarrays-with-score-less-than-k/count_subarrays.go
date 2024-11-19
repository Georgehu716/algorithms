package leetcode

func countSubarrays(nums []int, k int64) (ans int64) {
	left, s := 0, 0
	for right, x := range nums {
		s += x
		for int64(s * (right - left + 1)) >= k {
			s -= nums[left]
			left++
		}
		ans += int64(right - left + 1)
	}
	return
}
