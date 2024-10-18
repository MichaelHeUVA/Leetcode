# https://leetcode.com/problems/network-delay-time/description/
from collections import defaultdict
from heapq import heappop, heappush
from typing import List


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # make graph
        adj_list = defaultdict(list)
        for u, v, w in times:
            adj_list[u].append((v, w))
        # dijkstras algorithm
        pq = []
        heappush(pq, (0, k))
        dist = [float("inf")] * (n + 1)
        dist[0] = 0
        dist[k] = 0

        while pq:
            d, u = heappop(pq)

            for v, w in adj_list[u]:
                if dist[v] > dist[u] + w:
                    dist[v] = dist[u] + w
                    heappush(pq, (dist[v], v))
        delay = max(dist)
        return -1 if delay == float("inf") else delay
