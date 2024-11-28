# https://leetcode.com/problems/minimum-obstacle-removal-to-reach-corner/?envType=daily-question&envId=2024-11-28
from collections import defaultdict
from heapq import heappop, heappush
from typing import List


class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        pq = [(grid[0][0], 0, 0)]
        dist = [[float('inf')] * cols for _ in range(rows)]
        dist[0][0] = grid[0][0]
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while pq:
            d, row, col = heappop(pq)

            if row == rows - 1 and col == cols - 1:
                return d

            for dr, dc in directions:
                new_row = row + dr
                new_col = col + dc
                if new_row >= 0 and new_row < rows and new_col >= 0 and new_col < cols:
                    if dist[new_row][new_col] > d + grid[new_row][new_col]:
                        dist[new_row][new_col] = d + grid[new_row][new_col]
                        heappush(pq, (dist[new_row][new_col], new_row, new_col))

        return dist[rows - 1][cols - 1]
