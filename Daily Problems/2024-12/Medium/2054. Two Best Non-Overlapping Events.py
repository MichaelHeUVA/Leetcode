# https://leetcode.com/problems/two-best-non-overlapping-events/?envType=daily-question&envId=2024-12-08
from typing import List


class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        times = []

        for start, end, value in events:
            times.append((start, "start", value))
            times.append((end + 1, "end", value))

        times.sort()
        output = 0
        max_value = 0
        for _, start_or_end, value in times:
            if start_or_end == "start":
                output = max(output, value + max_value)
            else:
                max_value = max(max_value, value)
        return output
