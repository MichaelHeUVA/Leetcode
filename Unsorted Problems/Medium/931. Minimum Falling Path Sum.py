# https://leetcode.com/problems/minimum-falling-path-sum/description/
from typing import List


class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])
        dp = [[float("inf")] * cols for _ in range(rows)]
        for col in range(cols):
            dp[0][col] = matrix[0][col]
        for row in range(1, rows):
            for col in range(cols):
                if col - 1 >= 0:
                    dp[row][col] = min(
                        dp[row][col], dp[row - 1][col - 1] + matrix[row][col]
                    )
                if col + 1 < cols:
                    dp[row][col] = min(
                        dp[row][col], dp[row - 1][col + 1] + matrix[row][col]
                    )
                dp[row][col] = min(dp[row][col], dp[row - 1][col] + matrix[row][col])
        return min(dp[-1])
