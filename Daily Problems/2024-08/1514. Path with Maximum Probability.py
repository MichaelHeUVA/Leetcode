# https://leetcode.com/problems/path-with-maximum-probability/description/?envType=daily-question&envId=2024-08-31
from collections import defaultdict
import heapq
from typing import List


class Solution:
    def maxProbability(
        self,
        n: int,
        edges: List[List[int]],
        succProb: List[float],
        start_node: int,
        end_node: int,
    ) -> float:
        adj_list = defaultdict(list)
        for (u, v), w in zip(edges, succProb):
            adj_list[u].append((v, w))
            adj_list[v].append((u, w))
        dist = [0] * n
        pq = []
        heapq.heappush(pq, (-1.0, start_node))

        while pq:
            d, u = heapq.heappop(pq)
            d = -d
            for v, w in adj_list[u]:
                if dist[v] < (d * w):
                    dist[v] = d * w
                    heapq.heappush(pq, (-dist[v], v))
        return dist[end_node]
