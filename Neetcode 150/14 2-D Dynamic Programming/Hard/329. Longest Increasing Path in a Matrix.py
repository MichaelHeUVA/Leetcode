# https://leetcode.com/problems/longest-increasing-path-in-a-matrix/description/
from typing import List


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        max_length = 0
        dp = {}
        rows = len(matrix)
        cols = len(matrix[0])

        def dfs(row, col, prev):
            if (row, col) in dp and prev < matrix[row][col]:
                return dp[(row, col)]

            if (
                row >= rows
                or col >= cols
                or row < 0
                or col < 0
                or prev >= matrix[row][col]
            ):
                return 0

            dp[(row, col)] = max(
                dfs(row, col + 1, matrix[row][col]) + 1,
                dfs(row, col - 1, matrix[row][col]) + 1,
                dfs(row + 1, col, matrix[row][col]) + 1,
                dfs(row - 1, col, matrix[row][col]) + 1,
            )
            return dp[(row, col)]

        for row in range(rows):
            for col in range(cols):
                max_length = max(max_length, dfs(row, col, -1))

        return max_length
