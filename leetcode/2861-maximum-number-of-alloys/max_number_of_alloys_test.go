package leetcode

import "testing"

func TestMaxNumberOfAlloys(t *testing.T) {
	testCases := []struct{
		n int
		k int
		budget int
		composition [][]int
		stock []int
		cost []int
		ans int
	}{
		{3, 2, 15, [][]int{{1, 1, 1}, {1, 1, 10}}, []int{0, 0, 0}, []int{1, 2, 3}, 2},
	}

	for _, tc := range testCases {
		result := maxNumberOfAlloys(tc.n, tc.k, tc.budget, tc.composition, tc.stock, tc.cost)
		if result != tc.ans {
			t.Errorf("maxNumberOfAlloys(%d, %d, %d, %v, %v, %v) = %d; expected: %d",
				tc.n,
				tc.k,
				tc.budget,
				tc.composition,
				tc.stock,
				tc.cost,
				result,
				tc.ans)
		}
	}
}
