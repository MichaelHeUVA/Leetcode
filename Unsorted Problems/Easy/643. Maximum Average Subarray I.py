# https://leetcode.com/problems/maximum-average-subarray-i/description/
from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        res = 0
        for i in range(k):
            res += nums[i]
        maximum = res
        left = 0
        for right in range(k, len(nums)):
            res += nums[right]
            res -= nums[left]
            left += 1
            maximum = max(maximum, res)
        return maximum / k
