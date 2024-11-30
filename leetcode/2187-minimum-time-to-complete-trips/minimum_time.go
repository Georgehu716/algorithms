package leetcode

import "slices"

func minimumTime(time []int, totalTrips int) int64 {
	minT := slices.Min(time)
	maxT := slices.Max(time)
	avg := (totalTrips - 1) / len(time) + 1

	left := minT * avg - 1
	right := min(maxT * avg, minT * totalTrips)
	for left + 1 < right {
		mid := (left + right) / 2
		sum := 0
		for _, t := range time {
			sum += mid / t
		}
		if sum >= totalTrips {
			right = mid
		} else {
			left = mid
		}
	}
	return int64(right)
}
