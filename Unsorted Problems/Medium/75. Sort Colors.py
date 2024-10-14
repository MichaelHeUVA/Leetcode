# https://leetcode.com/problems/sort-colors/description/
from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        current = 0
        left = 0
        right = len(nums) - 1

        while current <= right:
            if nums[current] == 0:
                nums[current], nums[left] = nums[left], nums[current]
                left += 1
                current += 1
            elif nums[current] == 2:
                nums[current], nums[right] = nums[right], nums[current]
                right -= 1
            else:
                current += 1
