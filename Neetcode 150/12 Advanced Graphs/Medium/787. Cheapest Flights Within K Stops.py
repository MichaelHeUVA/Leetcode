# https://leetcode.com/problems/cheapest-flights-within-k-stops/description/
from collections import defaultdict
from heapq import heappop, heappush
from typing import List


class Solution:
    def findCheapestPrice(
        self, n: int, flights: List[List[int]], src: int, dst: int, k: int
    ) -> int:
        adj_list = defaultdict(list)
        for start, end, price in flights:
            adj_list[start].append((end, price))

        pq = [(0, src, 0)]
        distances = [float("inf")] * n
        distances[src] = 0
        while pq:
            dist, u, stops = heappop(pq)
            if stops <= k:
                for v, w in adj_list[u]:
                    distances[v] = dist + w
                    heappush(pq, (distances[v], v, stops + 1))

        return distances[dst] if distances[dst] != float("inf") else -1
