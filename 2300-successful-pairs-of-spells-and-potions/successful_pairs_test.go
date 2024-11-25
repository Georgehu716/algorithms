package leetcode

import (
	"testing"
	"reflect"
)

func TestSuccessfulPairs(t *testing.T) {
	testCases := []struct{
		spells []int
		potions []int
		success int64
		ans []int
	}{
		{[]int{5, 1, 3}, []int{1, 2, 3, 4, 5}, 7, []int{4, 0, 3}},
		{[]int{3, 1, 2}, []int{8, 5, 8}, 16, []int{2, 0, 2}},
	}

	for _, tc := range testCases {
		result := successfulPairs(tc.spells, tc.potions, tc.success)
		if !reflect.DeepEqual(result, tc.ans) {
			t.Errorf("successfulPairs(%v, %v, %d) = %v; expected: %v", tc.spells, tc.potions, tc.success, result, tc.ans)
		}
	}
}
