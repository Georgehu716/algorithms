package leetcode

import "testing"

func TestQuery(t *testing.T) {
	testCases := []struct{
		arr []int
		query []struct{
			left int
			right int
			value int
			ans int
		}
	}{
		{
			arr: []int{12, 33, 4, 56, 22, 2, 34, 33, 22, 12, 34, 56}, 
			query: []struct{
				left int
				right int
				value int
				ans int
			}{
				{left: 1, right: 2, value: 4, ans: 1},
				{left: 0, right: 11, value: 33, ans: 2},
			},
		},
		{
			arr: []int{2, 2, 1, 2, 2},
			query: []struct{
				left int
				right int
				value int
				ans int
			}{
				{left: 2, right: 4, value: 1, ans: 1},
				{left: 1, right: 3, value: 1, ans: 1},
				{left: 0, right: 2, value: 1, ans: 1},
			},
		},
	}

	for _, tc := range testCases {
		obj := Constructor(tc.arr)
		for _, q := range tc.query {
			result := obj.Query(q.left, q.right, q.value)
			if result != q.ans {
				t.Errorf("Query(%d, %d, %d) = %d; expected: %d", q.left, q.right, q.value, result, q.ans)
			}
		}
	}
}
