# https://leetcode.com/problems/minimum-operations-to-make-the-array-increasing/description/
from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        output = 0
        for i in range(1, len(nums)):
            if nums[i - 1] >= nums[i]:
                output += nums[i - 1] - nums[i] + 1
                nums[i] = nums[i - 1] + 1
        return output
