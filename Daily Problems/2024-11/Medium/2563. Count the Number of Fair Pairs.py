# https://leetcode.com/problems/count-the-number-of-fair-pairs/description/?envType=daily-question&envId=2024-11-13
from typing import List


class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        n = len(nums)
        output = 0
        for i in range(n - 1):
            left = i + 1
            right = n - 1
            while left <= right:
                mid = (left + right) // 2
                if lower <= nums[mid] + nums[i]:
                    right = mid - 1
                else:
                    left = mid + 1
            left_bound = left
            left = i + 1
            right = n - 1

            while left <= right:
                mid = (left + right) // 2
                if nums[mid] + nums[i] <= upper:
                    left = mid + 1
                else:
                    right = mid - 1
            right_bound = left
            output += right_bound - left_bound
        return output
