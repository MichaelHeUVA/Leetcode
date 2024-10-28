# https://leetcode.com/problems/find-peak-element/description/
from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if mid - 1 < 0:
                mid_left = float("-inf")
            else:
                mid_left = nums[mid - 1]
            if mid + 1 >= len(nums):
                mid_right = float("-inf")
            else:
                mid_right = nums[mid + 1]
            if mid_left < nums[mid] > mid_right:
                return mid
            elif mid_left < nums[mid] < mid_right:
                left = mid + 1
            else:
                right = mid - 1
