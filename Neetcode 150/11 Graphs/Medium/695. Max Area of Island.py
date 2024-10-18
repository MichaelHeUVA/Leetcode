# https://leetcode.com/problems/max-area-of-island/description/
from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        max_area = 0

        def dfs(row, col):
            if row < 0 or row == rows or col < 0 or col == cols or grid[row][col] == 0:
                return 0
            grid[row][col] = 0
            return (
                1
                + dfs(row + 1, col)
                + dfs(row - 1, col)
                + dfs(row, col + 1)
                + dfs(row, col - 1)
            )

        for row in range(rows):
            for col in range(cols):
                max_area = max(max_area, dfs(row, col))
        return max_area
