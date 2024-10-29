# https://leetcode.com/problems/maximum-number-of-moves-in-a-grid/description/?envType=daily-question&envId=2024-10-29
from typing import List


class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        dp = [[0] * cols for _ in range(rows)]
        for row in range(rows):
            dp[row][0] = 1
        max_moves = 0
        for col in range(1, cols):
            for row in range(rows):
                if grid[row][col - 1] < grid[row][col] and dp[row][col - 1] > 0:
                    dp[row][col] = max(dp[row][col], dp[row][col - 1] + 1)
                if (
                    row - 1 >= 0
                    and grid[row - 1][col - 1] < grid[row][col]
                    and dp[row - 1][col - 1] > 0
                ):
                    dp[row][col] = max(dp[row][col], dp[row - 1][col - 1] + 1)
                if (
                    row + 1 < rows
                    and grid[row + 1][col - 1] < grid[row][col]
                    and dp[row + 1][col - 1] > 0
                ):
                    dp[row][col] = max(dp[row][col], dp[row + 1][col - 1] + 1)
                max_moves = max(max_moves, dp[row][col] - 1)
        return max_moves
