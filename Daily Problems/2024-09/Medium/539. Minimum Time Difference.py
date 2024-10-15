# https://leetcode.com/problems/minimum-time-difference/description/?envType=daily-question&envId=2024-09-16
from typing import List


class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        time_in_seconds = []
        for times in timePoints:
            time_in_seconds.append(int(times[:2]) * 60 + int(times[3:5]))
        time_in_seconds.sort()
        min_diff = float("inf")
        for i in range(len(time_in_seconds) - 1):
            min_diff = min(min_diff, time_in_seconds[i + 1] - time_in_seconds[i])
        min_diff = min(min_diff, 1440 - time_in_seconds[-1] + time_in_seconds[0])
        return min_diff
