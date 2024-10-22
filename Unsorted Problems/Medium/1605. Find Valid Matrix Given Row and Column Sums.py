# https://leetcode.com/problems/find-valid-matrix-given-row-and-column-sums/description/
from typing import List


class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        rows = len(rowSum)
        cols = len(colSum)
        output = [[0] * cols for _ in range(rows)]
        for row in range(rows):
            for col in range(cols):
                output[row][col] = min(rowSum[row], colSum[col])

                rowSum[row] -= output[row][col]
                colSum[col] -= output[row][col]

        return output
