# https://leetcode.com/problems/count-alternating-subarrays/description/
from typing import List


class Solution:
    def countAlternatingSubarrays(self, nums: List[int]) -> int:
        output = 0
        streak = 0
        for i in range(len(nums)):
            if nums[i] != nums[i - 1]:
                streak += 1
            else:
                streak = 1
            output += streak
        return output
