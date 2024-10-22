# https://leetcode.com/problems/count-days-without-meetings/description/
from typing import List


class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        prev_start, prev_end = meetings[0]
        busy_days = 0
        for i in range(1, len(meetings)):
            start, end = meetings[i]
            if prev_end >= start:
                prev_end = max(prev_end, end)
            else:
                busy_days += prev_end - prev_start + 1
                prev_start = start
                prev_end = end
        busy_days += prev_end - prev_start + 1
        return days - busy_days
