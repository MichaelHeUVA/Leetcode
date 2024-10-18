# https://leetcode.com/problems/min-cost-to-connect-all-points/description/
from collections import defaultdict
from heapq import heappop, heappush
from typing import List


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # building adjacency list
        n = len(points)
        adj_list = defaultdict(list)  # neighboring lists has lists of [cost, node]
        for i in range(n):
            xi, yi = points[i]
            for j in range(i + 1, n):
                xj, yj = points[j]
                distance = abs(xi - xj) + abs(yi - yj)
                adj_list[i].append([distance, j])
                adj_list[j].append([distance, i])

        # prim's algorithm
        total_cost = 0
        min_heap = [[0, 0]]  # [cost, node]
        visited = set()
        while len(visited) < n:
            cost, node = heappop(min_heap)
            if node in visited:
                continue
            total_cost += cost
            visited.add(node)
            for neighbor_cost, neighbor_node in adj_list[node]:
                if neighbor_node not in visited:
                    heappush(min_heap, [neighbor_cost, neighbor_node])

        return total_cost
