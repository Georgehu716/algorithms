package leetcode

func findPeakGrid(mat [][]int) []int {
	left, right := 0, len(mat) - 2
	for left <= right {
		i := left + (right - left) / 2
		j := indexOfMax(mat[i])
		if mat[i][j] > mat[i+1][j] {
			right = i - 1
		} else {
			left = i + 1
		}
	}
	return []int{left, indexOfMax(mat[left])}
}

func indexOfMax(a []int) (idx int) {
	for i, x := range a {
		if x > a[idx] {
			idx = i
		}
	}
	return
}
