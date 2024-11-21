# https://leetcode.com/problems/count-unguarded-cells-in-the-grid/?envType=daily-question&envId=2024-11-21
from typing import List


class Solution:
    def countUnguarded(
        self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]
    ) -> int:
        grid = [[0] * n for _ in range(m)]
        for row, col in walls:
            grid[row][col] = "W"
        for row, col in guards:
            grid[row][col] = "G"
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        def dfs(row, col, dr, dc):
            if (
                row >= m
                or col >= n
                or row < 0
                or col < 0
                or grid[row][col] == "W"
                or grid[row][col] == "G"
            ):
                return
            grid[row][col] = 1
            row += dr
            col += dc
            dfs(row, col, dr, dc)

        for row, col in guards:
            for dr, dc in directions:
                dfs(row + dr, col + dc, dr, dc)

        output = 0
        for row in grid:
            for cell in row:
                if cell == 0:
                    output += 1
        return output
