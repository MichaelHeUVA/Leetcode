# https://leetcode.com/problems/teemo-attacking/description/
from typing import List


class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        poisoned_time = 0
        for i in range(len(timeSeries) - 1):
            if timeSeries[i + 1] - timeSeries[i] < duration:
                poisoned_time += timeSeries[i + 1] - timeSeries[i]
            else:
                poisoned_time += duration

        poisoned_time += duration

        return poisoned_time
