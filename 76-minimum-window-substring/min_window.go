package leetcode

func minWindow(s string, t string) string {
	cnt := make(map[rune]int)
	less := 0
	for _, c := range t {
		if cnt[c] == 0 {
			less++
		}
		cnt[c]++
	}

	left := 0
	ans := ""
	ans_len := len(s) + 1
	for right, c := range s {
		cnt[c]--
		if cnt[c] == 0 {
			less--
		}
		for less == 0 {
			if right - left + 1 < ans_len {
				ans_len = right - left + 1
				ans = s[left:right+1]
			}
			x := rune(s[left])
			if cnt[x] == 0 {
				less++
			}
			cnt[x]++
			left++
		}
	}
	return ans
}
