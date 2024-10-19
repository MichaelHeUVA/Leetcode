# https://leetcode.com/problems/minimum-interval-to-include-each-query/description/
from heapq import heappush, heappop
from typing import List


class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        m = {}  # {query: size}
        pq = []
        intervals.sort()
        i = 0
        for q in sorted(queries):
            while i < len(intervals) and intervals[i][0] <= q:
                start, end = intervals[i]
                size = end - start + 1
                heappush(pq, (size, end))
                i += 1
            while pq and pq[0][1] < q:
                heappop(pq)
            if pq:
                m[q] = pq[0][0]
            else:
                m[q] = -1

        output = []
        for q in queries:
            output.append(m[q])

        return output
