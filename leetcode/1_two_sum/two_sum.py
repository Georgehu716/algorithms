"""
1. Two Sum

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.


Example 1:
Input: nums = [2, 7, 11, 15], target = 9
Output: [0, 1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
"""


class Solution:
    def two_sum(self, nums: List[int], target: int) -> List[int]:
        """
        1. brute force
        TIME: O(n^2)
        SPACE: O(1)
        """

        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []


        """
        2. hash map
        TIME: O(n)
        SPACE: O(n)
        """
        hash_d = {}
        for index, num in enumerate(nums):
            if target - num in hash_d:
                return [index, hash_d[target-num]]
            hash_d[num] = index
        return []
