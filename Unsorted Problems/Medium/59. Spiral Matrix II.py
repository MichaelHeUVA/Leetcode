# https://leetcode.com/problems/spiral-matrix-ii/description/
from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0] * n for _ in range(n)]
        left = top = 0
        right = bot = len(matrix)
        count = 1
        while left < right and top < bot:
            for i in range(left, right):
                matrix[top][i] = count
                count += 1
            top += 1
            for i in range(top, bot):
                matrix[i][right - 1] = count
                count += 1
            right -= 1
            for i in range(right - 1, left - 1, -1):
                matrix[bot - 1][i] = count
                count += 1
            bot -= 1
            for i in range(bot - 1, top - 1, -1):
                matrix[i][left] = count
                count += 1
            left += 1
        return matrix
