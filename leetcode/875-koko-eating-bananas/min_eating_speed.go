package leetcode

import "slices"

func minEatingSpeed(piles []int, h int) int {
	n := len(piles)
	left := 0
	right := slices.Max(piles)
	for left + 1 < right {
		mid := left + (right - left) / 2
		sum := n
		for _, p := range piles {
			sum += (p - 1) / mid
		}
		if sum <= h {
			right = mid
		} else {
			left = mid
		}
	}
	return right
}
