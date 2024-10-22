# https://leetcode.com/problems/next-permutation/description/
from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Find the first time the pattern decreases
        i = len(nums) - 2
        while i >= 0:
            if nums[i] < nums[i + 1]:
                break
            i -= 1
        if i == -1:
            nums.reverse()
            return
        j = i + 1
        min_greater_num = j
        # Find the element that is the smallest number that is larger than i
        while j < len(nums):
            if nums[j] > nums[i] and nums[min_greater_num] >= nums[j]:
                min_greater_num = j
            j += 1
        nums[i], nums[min_greater_num] = nums[min_greater_num], nums[i]

        def reverse(start):
            i = start
            j = len(nums) - 1
            while i < j:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1

        reverse(i + 1)
