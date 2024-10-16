# https://leetcode.com/problems/k-closest-points-to-origin/description/
from heapq import heappush, heappushpop
import math
from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def dist(x, y):
            return math.sqrt(pow(x, 2) + pow(y, 2))

        heap = []
        for x, y in points:
            distance = -dist(x, y)
            if len(heap) == k:
                heappushpop(heap, (distance, x, y))
            else:
                heappush(heap, (distance, x, y))
        result = []
        for dist, x, y in heap:
            result.append([x, y])
        return result
