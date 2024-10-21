# https://leetcode.com/problems/meeting-rooms-ii/description/
from heapq import heappush, heappushpop
from typing import List


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        heap = []
        for start, end in intervals:
            if heap and heap[0] <= start:
                heappushpop(heap, end)
            else:
                heappush(heap, end)

        return len(heap)
