# https://leetcode.com/problems/number-of-enclaves/description/
from typing import List


class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        def dfs(row, col):
            if row < 0 or row >= rows or col < 0 or col >= cols or grid[row][col] == 0:
                return
            grid[row][col] = 0
            dfs(row + 1, col)
            dfs(row - 1, col)
            dfs(row, col + 1)
            dfs(row, col - 1)

        for row in range(rows):
            dfs(row, 0)
            dfs(row, cols - 1)

        for col in range(cols):
            dfs(0, col)
            dfs(rows - 1, col)

        output = 0
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    output += 1
        return output
