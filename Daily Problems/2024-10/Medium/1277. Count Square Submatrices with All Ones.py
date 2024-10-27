# https://leetcode.com/problems/count-square-submatrices-with-all-ones/description/?envType=daily-question&envId=2024-10-27
from typing import List


class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])
        dp = [[0] * (cols + 1) for _ in range(rows + 1)]
        output = 0
        for row in range(1, rows + 1):
            for col in range(1, cols + 1):
                if matrix[row - 1][col - 1] == 1:
                    dp[row][col] = (
                        min(dp[row][col - 1], dp[row - 1][col], dp[row - 1][col - 1])
                        + 1
                    )
                    output += dp[row][col]
        return output
