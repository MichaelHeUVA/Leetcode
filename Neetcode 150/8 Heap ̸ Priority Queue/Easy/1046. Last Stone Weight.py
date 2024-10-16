# https://leetcode.com/problems/last-stone-weight/description/
from heapq import heappop, heappush


class Solution(object):
    def lastStoneWeight(self, stones):
        heap = []
        for stone in stones:
            heappush(heap, -stone)

        while heap and len(heap) != 1:
            a = -heappop(heap)
            b = -heappop(heap)
            if a != b:
                heappush(heap, b - a)

        if len(heap) == 1:
            return -heap[0]
        return 0
