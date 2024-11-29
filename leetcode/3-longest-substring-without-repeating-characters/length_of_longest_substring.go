package leetcode

func lengthOfLongestSubstring(s string) (ans int) {
	window := make(map[rune]bool)
	for right, c := range s {
		for window[c] {
			delete(window, rune(s[right - len(window)]))
		}
		window[c] = true
		ans = max(ans, len(window))
	}
	return
}
