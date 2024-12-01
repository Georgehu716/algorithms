package leetcode

import (
	"slices"
	"sort"
)

func maxNumberOfAlloys(n int, k int, budget int, composition [][]int, stock []int, cost []int) (ans int) {
	mx := slices.Min(stock) + budget
	for _, comp := range composition {
		ans += sort.Search(mx-ans, func(num int) bool {
			num += ans + 1
			money := 0
			for i, s := range stock {
				if s < comp[i] * num {
					money += (comp[i] * num - s) * cost[i]
					if money > budget {
						return true
					}
				}
			}
			return false
		})
	}
	return
}
