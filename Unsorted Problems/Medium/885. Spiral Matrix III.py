# https://leetcode.com/problems/spiral-matrix-iii/description/
from typing import List


class Solution:
    def spiralMatrixIII(
        self, rows: int, cols: int, rStart: int, cStart: int
    ) -> List[List[int]]:
        output = [[rStart, cStart]]
        iterations = rows * cols
        row = rStart
        col = cStart
        i = 1
        right = 1
        down = 1
        left = 2
        up = 2
        while i < iterations:
            count = 0
            while count < right:
                col += 1
                if row >= 0 and col >= 0 and row < rows and col < cols:
                    output.append([row, col])
                    i += 1
                count += 1
            right += 2

            count = 0
            while count < down:
                row += 1
                if row >= 0 and col >= 0 and row < rows and col < cols:
                    output.append([row, col])
                    i += 1
                count += 1
            down += 2

            count = 0
            while count < left:
                col -= 1
                if row >= 0 and col >= 0 and row < rows and col < cols:
                    output.append([row, col])
                    i += 1
                count += 1
            left += 2

            count = 0
            while count < up:
                row -= 1
                if row >= 0 and col >= 0 and row < rows and col < cols:
                    output.append([row, col])
                    i += 1
                count += 1
            up += 2

        return output
