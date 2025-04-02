"""
You've given an array of numbers and you need to find a pair of numbers that are equal to the given target value.
Numbers can be either positive, negative, or both.
Can you design an algorithm that works in O(n)-linear time or greater?

let sequence = [8, 10, 2, 9, 7, 5]
let results = pairValue(sum: 11) = // return (9, 2)
"""


import unittest


def pair_numbers_brute_force(nums: list[int], target: int) -> list[int]:
    """
    Brute force approach
    TIME: O(n^2)
    SPACE: O(1)
    """
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [nums[i], nums[j]]
    return []


def pair_numbers_memoized(nums: list[int], target: int) -> list[int]:
    """
    Memoized approach
    TIME: O(n)
    SPACE: O(n)
    """
    cache = set()
    for x in nums:
        diff = target - x
        if diff in cache:
            return [x, diff]
        cache.add(x)
    return []


class Solution(unittest.TestCase):
    def test_brute_force(self):
        self.assertEqual(pair_numbers_brute_force([8, 10, 2, 9, 7, 5], 11), [2, 9])
        self.assertEqual(pair_numbers_brute_force([1, 2, 3], 6), [])
        self.assertEqual(pair_numbers_brute_force([3, 1, 4, 6], 10), [4, 6])


    def test__memoized(self):
        self.assertEqual(pair_numbers_memoized([8, 10, 2, 9, 7, 5], 11), [9, 2])
        self.assertEqual(pair_numbers_memoized([1, 2, 3], 6), [])
        self.assertEqual(pair_numbers_memoized([3, 1, 4, 6], 10), [6, 4])


if __name__ == "__main__":
    unittest.main()
