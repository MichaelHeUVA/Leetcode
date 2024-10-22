# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/
from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        minimum = float("inf")
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            minimum = min(nums[mid], minimum)
            if nums[left] <= nums[mid]:
                if nums[mid] >= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                if nums[mid] >= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return minimum
