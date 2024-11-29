package leetcode

func longestSemiRepetitiveSubstring(s string) (ans int) {
	same, left := 0, 0
	for right, _ := range s {
		if right > 0 && s[right] == s[right-1] {
			same++
		}
		for same > 1 {
			if s[left] == s[left + 1] {
				same--
			}
			left++
		}
		ans = max(ans, right - left + 1)
	}
	return
}
