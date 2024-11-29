# https://leetcode.com/problems/shortest-distance-after-road-addition-queries-i/description/?envType=daily-question&envId=2024-11-27
from collections import defaultdict
from heapq import heappop, heappush
from typing import List


class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        adj_list = defaultdict(list)
        adj_list[0].append(1)
        for i in range(1, n - 1):
            adj_list[i].append(i + 1)

        def bfs():
            pq = [(0, 0)]
            dist = [float('inf')] * n
            while pq:
                d, u = heappop(pq)
                for v in adj_list[u]:
                    if v == n - 1:
                        return d + 1
                    if dist[v] > d + 1:
                        dist[v] = d + 1
                        heappush(pq, (dist[v], v))
            return dist[n - 1]

        output = []  
        for u, v in queries:
            adj_list[u].append(v)
            output.append(bfs())
        return output
