# https://leetcode.com/problems/non-overlapping-intervals/description/
from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        output = 0
        last_end = float("-inf")
        for start, end in intervals:
            if start >= last_end:
                last_end = end
            else:
                output += 1
        return output
