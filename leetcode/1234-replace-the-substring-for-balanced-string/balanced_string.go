package leetcode

func balancedString(s string) int {
	cnt, m := make(map[rune]int), len(s) / 4
	for _, c := range s {
		cnt[c]++
	}
	if cnt['Q'] == m && cnt['W'] == m && cnt['E'] == m && cnt['R'] == m {
		return 0
	}

	ans, left := len(s), 0
	for right, c := range s {
		cnt[c]--
		for cnt['Q'] <= m && cnt['W'] <=m && cnt['E'] <= m && cnt['R'] <=m {
			ans = min(ans, right - left + 1)
			cnt[rune(s[left])]++
			left++
		}
	}
	return ans
}
