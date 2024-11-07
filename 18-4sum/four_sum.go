package leetcode

import "slices"

func fourSum(nums []int, target int) (ans [][]int) {
	slices.Sort(nums)
	n := len(nums)

	for i := 0; i < n - 3; i++ {
		if i > 0 && nums[i] == nums[i - 1] {
			continue
		}
		if nums[i] + nums[i + 1] + nums[i + 2] + nums[i + 3] > target {
			break
		}
		if nums[i] + nums[n - 3] + nums[n - 2] + nums[n - 1] < target {
			continue
		}
		for j := i + 1; j < n - 2; j++ {
			if j > i + 1 && nums[j] == nums[j - 1] {
				continue
			}
			if nums[i] + nums[j] + nums[j + 1] + nums[j + 2] > target {
				break
			}
			if nums[i] + nums[j] + nums[n - 2] + nums[n - 1] < target {
				continue
			}
			k, l := j + 1, n - 1
			for k < l {
				s := nums[i] + nums[j] + nums[k] + nums[l]
				if s > target {
					l--
				} else if s < target {
					k++
				} else {
					ans = append(ans, []int{nums[i], nums[j], nums[k], nums[l]})
					for k++; k < l && nums[k] == nums[k - 1]; k++ {}
					for l--; l > k && nums[l] == nums[l + 1]; l-- {}
				}
			}
		}
	}
	return
}
