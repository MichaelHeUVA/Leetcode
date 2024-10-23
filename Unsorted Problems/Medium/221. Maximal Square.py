# https://leetcode.com/problems/maximal-square/description/
from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])
        dp = [[0] * (cols + 1) for _ in range(rows + 1)]
        max_side_length = 0
        for row in range(1, rows + 1):
            for col in range(1, cols + 1):
                if matrix[row - 1][col - 1] == "1":
                    dp[row][col] = (
                        min(dp[row][col - 1], dp[row - 1][col], dp[row - 1][col - 1])
                        + 1
                    )
                    max_side_length = max(max_side_length, dp[row][col])
        return max_side_length * max_side_length
