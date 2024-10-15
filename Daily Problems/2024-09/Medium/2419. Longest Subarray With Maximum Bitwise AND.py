# https://leetcode.com/problems/longest-subarray-with-maximum-bitwise-and/description/?envType=daily-question&envId=2024-09-14
from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        max_num = nums[0]
        max_streak = 0
        current_streak = 0
        for num in nums:
            if num > max_num:
                max_num = num
                max_streak = 0
                current_streak = 0
            if max_num == num:
                current_streak += 1
            else:
                current_streak = 0
            max_streak = max(max_streak, current_streak)
        return max_streak
