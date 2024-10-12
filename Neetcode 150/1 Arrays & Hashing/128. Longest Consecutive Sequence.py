# https://leetcode.com/problems/longest-consecutive-sequence/description/
from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        longest = 0
        for num in s:
            if (num - 1) not in s:
                temp = 1
                while num + 1 in s:
                    num += 1
                    temp += 1
                longest = max(longest, temp)

        return longest
