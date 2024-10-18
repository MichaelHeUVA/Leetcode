# https://leetcode.com/problems/number-of-islands/description/
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        number_of_islands = 0
        rows = len(grid)
        cols = len(grid[0])

        def dfs(row, col):
            if (
                row < 0
                or col < 0
                or row >= rows
                or col >= cols
                or grid[row][col] == "0"
            ):
                return
            grid[row][col] = "0"
            dfs(row + 1, col)
            dfs(row - 1, col)
            dfs(row, col + 1)
            dfs(row, col - 1)

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1":
                    number_of_islands += 1
                    dfs(row, col)
        return number_of_islands
