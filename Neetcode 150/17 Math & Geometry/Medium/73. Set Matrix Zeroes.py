# https://leetcode.com/problems/set-matrix-zeroes/description/
from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])

        first_row_is_zero = False
        first_col_is_zero = False

        for row in range(m):
            for col in range(n):
                if matrix[row][col] == 0:
                    if row == 0:
                        first_row_is_zero = True
                    if col == 0:
                        first_col_is_zero = True
                    matrix[row][0] = matrix[0][col] = 0

        for row in range(1, m):
            for col in range(1, n):
                if matrix[0][col] == 0 or matrix[row][0] == 0:
                    matrix[row][col] = 0

        if first_row_is_zero:
            for col in range(n):
                matrix[0][col] = 0

        if first_col_is_zero:
            for row in range(m):
                matrix[row][0] = 0
