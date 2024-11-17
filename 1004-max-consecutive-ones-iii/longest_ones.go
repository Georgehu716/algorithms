package leetcode

func longestOnes(nums []int, k int) (ans int) {
	left, cnt0 := 0, 0
	for right, x := range nums {
		cnt0 += 1 - x
		for cnt0 > k {
			cnt0 -= 1 - nums[left]
			left++
		}
		ans = max(ans, right - left + 1)
	}
	return
}
