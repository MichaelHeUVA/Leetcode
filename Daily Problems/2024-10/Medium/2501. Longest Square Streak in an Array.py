# https://leetcode.com/problems/longest-square-streak-in-an-array/description/?envType=daily-question&envId=2024-10-28
from typing import List


class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        nums = set(nums)
        longest = 0
        for num in nums:
            temp = num
            count = 1
            while temp**2 in nums:
                temp = temp**2
                count += 1
            longest = max(longest, count)

        return -1 if longest == 1 else longest
