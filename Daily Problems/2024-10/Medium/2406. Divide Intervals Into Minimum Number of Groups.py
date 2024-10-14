# https://leetcode.com/problems/divide-intervals-into-minimum-number-of-groups/description/?envType=daily-question&envId=2024-10-12
from heapq import heappush, heappop
from typing import List


class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        heap = []
        for start, end in intervals:
            if heap and heap[0] < start:
                heappop(heap)
            heappush(heap, end)

        return len(heap)
