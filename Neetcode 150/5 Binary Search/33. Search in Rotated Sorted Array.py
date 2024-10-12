# https://leetcode.com/problems/search-in-rotated-sorted-array/description/
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        left = 0
        right = n - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            # if we are in the left sorted position
            elif nums[left] <= nums[mid]:
                if target < nums[left] or target > nums[mid]:
                    left = mid + 1
                else:
                    right = mid - 1
            # if we are in the right sorted position
            else:
                if target > nums[right] or target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
        return -1
