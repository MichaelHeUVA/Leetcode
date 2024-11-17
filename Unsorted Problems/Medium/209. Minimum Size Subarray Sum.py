# https://leetcode.com/problems/minimum-size-subarray-sum/description/
from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        left = 0
        output = float("inf")
        window = 0
        for right in range(n):
            window += nums[right]
            while window >= target:
                output = min(output, right - left + 1)
                window -= nums[left]
                left += 1

        return output if output != float("inf") else 0
