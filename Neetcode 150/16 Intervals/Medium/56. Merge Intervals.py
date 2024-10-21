# https://leetcode.com/problems/merge-intervals/description/
from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 1:
            return intervals
        intervals.sort()
        new_interval = intervals[0]
        output = []
        for start, end in intervals:
            if end < new_interval[0]:
                output.append([start, end])
            elif start > new_interval[1]:
                output.append(new_interval)
                new_interval = [start, end]
            else:
                new_interval = [min(start, new_interval[0]), max(end, new_interval[1])]
        output.append(new_interval)
        return output
