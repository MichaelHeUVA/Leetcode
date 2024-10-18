# https://leetcode.com/problems/pacific-atlantic-water-flow/description/
from typing import List


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])
        can_flow = []
        atl = set()
        pac = set()

        def dfs(row, col, prev_height, ocean):
            if (
                row < 0
                or col < 0
                or row >= rows
                or col >= cols
                or prev_height > heights[row][col]
                or (row, col) in ocean
            ):
                return
            ocean.add((row, col))
            dfs(row + 1, col, heights[row][col], ocean)
            dfs(row, col + 1, heights[row][col], ocean)
            dfs(row - 1, col, heights[row][col], ocean)
            dfs(row, col - 1, heights[row][col], ocean)

        for row in range(rows):
            dfs(row, 0, heights[row][0], pac)
            dfs(row, cols - 1, heights[row][cols - 1], atl)

        for col in range(cols):
            dfs(0, col, heights[0][col], pac)
            dfs(rows - 1, col, heights[rows - 1][col], atl)

        for row in range(rows):
            for col in range(cols):
                if (row, col) in atl and (row, col) in pac:
                    can_flow.append([row, col])

        return can_flow
