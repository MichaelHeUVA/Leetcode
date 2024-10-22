# https://leetcode.com/problems/minimum-path-sum/description/
from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        dp = {}  # {(row, col): dist}
        for row in range(rows - 1, -1, -1):
            for col in range(cols - 1, -1, -1):
                if row == rows - 1 and col != cols - 1:
                    dp[(row, col)] = grid[row][col] + dp[(row, col + 1)]
                elif row != rows - 1 and col == cols - 1:
                    dp[(row, col)] = grid[row][col] + dp[(row + 1, col)]
                elif row != rows - 1 and col != cols - 1:
                    dp[(row, col)] = grid[row][col] + min(
                        dp[(row, col + 1)], dp[(row + 1, col)]
                    )
                else:
                    dp[(row, col)] = grid[row][col]

        return dp[(0, 0)]
