# https://leetcode.com/problems/minimize-maximum-value-in-a-grid/description/?envType=weekly-question&envId=2024-11-22
from typing import List
from heapq import heappush, heappop


# Sort
class Solution:
    def minScore(self, grid: List[List[int]]) -> List[List[int]]:
        rows = len(grid)
        cols = len(grid[0])

        nums = []
        min_row = [1] * rows
        min_col = [1] * cols

        for row in range(rows):
            for col in range(cols):
                nums.append((grid[row][col], row, col))

        nums.sort()

        for _, row, col in nums:
            val = max(min_row[row], min_col[col])
            grid[row][col] = val
            min_row[row] = val + 1
            min_col[col] = val + 1

        return grid


# Heap / Priority Queue
class Solution:  # noqa: F811
    def minScore(self, grid: List[List[int]]) -> List[List[int]]:
        rows = len(grid)
        cols = len(grid[0])

        min_heap = []
        min_row = [1] * rows
        min_col = [1] * cols

        for row in range(rows):
            for col in range(cols):
                heappush(min_heap, (grid[row][col], row, col))

        while min_heap:
            _, row, col = heappop(min_heap)
            val = max(min_row[row], min_col[col])
            grid[row][col] = val
            min_row[row] = val + 1
            min_col[col] = val + 1

        return grid
