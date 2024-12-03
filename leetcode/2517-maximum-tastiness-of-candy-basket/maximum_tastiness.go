package leetcode

import "sort"

func maximumTastiness(price []int, k int) int {
	sort.Ints(price)
	return sort.Search((price[len(price) - 1] - price[0]) / (k - 1), func(d int) bool {
		d++
		cnt, pre := 1, price[0]
		for _, p := range price[1:] {
			if p >= pre + d {
				cnt++
				pre = p
			}
		}
		return cnt < k
	})
}
