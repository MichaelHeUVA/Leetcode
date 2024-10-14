# https://leetcode.com/problems/search-a-2d-matrix/description/
from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])

        top = 0
        bot = rows - 1
        while top <= bot:
            left = 0
            right = cols - 1
            midtb = (top + bot) // 2
            if matrix[midtb][0] <= target and target <= matrix[midtb][cols - 1]:
                while left <= right:
                    midlr = (left + right) // 2
                    if matrix[midtb][midlr] == target:
                        return True
                    if matrix[midtb][midlr] < target:
                        left = midlr + 1
                    elif matrix[midtb][midlr] > target:
                        right = midlr - 1
                return False
            elif matrix[midtb][0] > target:
                bot = midtb - 1
            elif matrix[midtb][cols - 1] < target:
                top = midtb + 1

        return False
