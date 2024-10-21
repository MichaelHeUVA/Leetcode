# https://leetcode.com/problems/rotate-image/description/
from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # flip on diagonal and swap columns
        rows = len(matrix)
        cols = len(matrix[0])
        for row in range(rows):
            for col in range(row, cols):
                if row != col:
                    matrix[row][col], matrix[col][row] = (
                        matrix[col][row],
                        matrix[row][col],
                    )

        for col in range(cols // 2):
            for row in range(rows):
                matrix[row][col], matrix[row][cols - col - 1] = (
                    matrix[row][cols - col - 1],
                    matrix[row][col],
                )

        return
