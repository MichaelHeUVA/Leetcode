# https://leetcode.com/problems/regions-cut-by-slashes/description/
from typing import List


class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        n = len(grid)
        scaled_grid = [[0] * (n * 3) for _ in range(n * 3)]

        for row in range(n):
            for col in range(n):
                if grid[row][col] == "/":
                    scaled_grid[(row * 3) + 2][(col * 3)] = 1
                    scaled_grid[(row * 3) + 1][(col * 3) + 1] = 1
                    scaled_grid[(row * 3)][(col * 3) + 2] = 1
                elif grid[row][col] == "\\":
                    scaled_grid[(row * 3)][(col * 3)] = 1
                    scaled_grid[(row * 3) + 1][(col * 3) + 1] = 1
                    scaled_grid[(row * 3) + 2][(col * 3) + 2] = 1

        rows = len(scaled_grid)
        cols = len(scaled_grid[0])
        output = 0

        def dfs(row, col):
            if (
                row < 0
                or col < 0
                or row >= rows
                or col >= cols
                or scaled_grid[row][col] == 1
            ):
                return
            scaled_grid[row][col] = 1
            dfs(row + 1, col)
            dfs(row - 1, col)
            dfs(row, col + 1)
            dfs(row, col - 1)

        for row in range(rows):
            for col in range(cols):
                if scaled_grid[row][col] == 0:
                    output += 1
                    dfs(row, col)

        return output
