# https://leetcode.com/problems/minimum-time-to-visit-a-cell-in-a-grid/description/?envType=daily-question&envId=2024-11-29
from heapq import heappop, heappush
from typing import List


class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:
        if grid[1][0] > 1 and grid[0][1] > 1:
            return -1
        rows = len(grid)
        cols = len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        pq = [(grid[0][0], 0, 0)]
        visited = set()
        while pq:
            time, row, col = heappop(pq)
            if (row, col) == (rows - 1, cols - 1):
                return time
            if (row, col) in visited:
                continue
            visited.add((row, col))

            for dr, dc in directions:
                new_row = row + dr
                new_col = col + dc

                if 0 <= new_row < rows and 0 <= new_col < cols:
                    wait_time = 1 if (grid[new_row][new_col] - time) % 2 == 0 else 0
                    new_time = max(grid[new_row][new_col] + wait_time, time + 1)
                    heappush(pq, (new_time, new_row, new_col))

        return -1
