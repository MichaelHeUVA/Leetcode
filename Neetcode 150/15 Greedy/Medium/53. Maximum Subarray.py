# https://leetcode.com/problems/maximum-subarray/description/
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        total = 0
        for num in nums:
            if total < 0:
                total = 0
            total += num
            max_sum = max(max_sum, total)
        return max_sum
