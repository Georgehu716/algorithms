package leetcode

import (
	"math"
	"sort"
)

func threeSumClosest(nums []int, target int) (ans int) {
	sort.Ints(nums)
	n := len(nums)
	minDiff := math.MaxInt

	for i, x := range nums[:n-2] {
		if i > 0 && nums[i] == nums[i - 1] {
			continue
		}
		s := x + nums[i + 1] + nums[i + 2]
		if s > target {
			if s - target < minDiff {
				ans = s
			}
			break
		}
		s = x + nums[n - 2] + nums[n - 1]
		if s < target {
			if target - s < minDiff {
				minDiff = target - s
				ans = s
			}
			continue
		}

		j, k := i + 1, n - 1
		for j < k {
			s = x + nums[j] + nums[k]
			if s == target {
				return target
			}
			if s < target {
				if s - target < minDiff {
					minDiff = s - target
					ans = s
				}
				j++
			} else {
				if target - s < minDiff {
					minDiff = target - s
					ans = s
				}
				k--
			}
		}
	}
	return ans
}
