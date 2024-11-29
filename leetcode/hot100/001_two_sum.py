import unittest
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_table = dict()
        for index, num in enumerate(nums):
            if target-num in hash_table:
                return [hash_table[target-num], index]
            hash_table[num] = index
        return []


class TestTwoSum(unittest.TestCase):

    def test_twoSum(self):
        self.assertEqual(Solution().twoSum([2, 3, 5, 7], 9), [0, 3])
        self.assertEqual(Solution().twoSum([], 8), [])


if __name__ == '__main__':
    unittest.main()
