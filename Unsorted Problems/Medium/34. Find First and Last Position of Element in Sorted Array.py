# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/
from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = 0
        right = len(nums) - 1
        left_bound = -1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] >= target:
                if nums[mid] == target:
                    left_bound = mid
                right = mid - 1
            else:
                left = mid + 1

        left = 0
        right = len(nums) - 1
        right_bound = -1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] <= target:
                if nums[mid] == target:
                    right_bound = mid
                left = mid + 1
            else:
                right = mid - 1

        return [left_bound, right_bound]
