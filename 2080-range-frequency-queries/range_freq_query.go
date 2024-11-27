package leetcode

import "sort"

type RangeFreqQuery map[int][]int

func Constructor(arr []int) RangeFreqQuery {
	pos := map[int][]int{}
	for i, x := range arr {
		pos[x] = append(pos[x], i)
	}
	return pos
}

func (pos RangeFreqQuery) Query(left int, right int, value int) int {
	a := pos[value]
	p := sort.SearchInts(a, left)
	return sort.SearchInts(a[p:], right+1)
}
