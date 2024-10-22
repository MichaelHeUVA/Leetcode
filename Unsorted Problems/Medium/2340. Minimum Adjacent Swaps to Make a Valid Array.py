# https://leetcode.com/problems/minimum-adjacent-swaps-to-make-a-valid-array/description/
from typing import List


class Solution:
    def minimumSwaps(self, nums: List[int]) -> int:
        max_index = 0
        min_index = 0
        for i in range(len(nums)):
            if nums[max_index] <= nums[i]:
                max_index = i
            if nums[min_index] > nums[i]:
                min_index = i

        if min_index == max_index:
            return 0
        if min_index < max_index:
            return min_index + ((len(nums) - 1) - max_index)
        else:
            return min_index + ((len(nums) - 1) - max_index) - 1
