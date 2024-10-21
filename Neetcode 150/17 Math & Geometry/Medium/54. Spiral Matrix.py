# https://leetcode.com/problems/spiral-matrix/description/
from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        left, top = 0, 0
        right, bot = len(matrix[0]), len(matrix)
        output = []
        while left < right and top < bot:
            for i in range(left, right):
                output.append(matrix[top][i])
            top += 1
            for i in range(top, bot):
                output.append(matrix[i][right - 1])
            right -= 1
            if not (left < right and top < bot):
                break
            for i in range(right - 1, left - 1, -1):
                output.append(matrix[bot - 1][i])
            bot -= 1
            for i in range(bot - 1, top - 1, -1):
                output.append(matrix[i][left])
            left += 1
        return output
