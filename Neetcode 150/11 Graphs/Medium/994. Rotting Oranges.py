# https://leetcode.com/problems/rotting-oranges/description/
from collections import deque
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh = 0
        time = 0
        queue = deque()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    fresh += 1
                if grid[i][j] == 2:
                    queue.append((i, j))
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        while queue and fresh > 0:
            rotten_oranges = len(queue)
            for i in range(rotten_oranges):
                i, j = queue.popleft()
                for r, c in directions:
                    row = i + r
                    col = j + c
                    if (
                        row in range(len(grid))
                        and col in range(len(grid[0]))
                        and grid[row][col] == 1
                    ):
                        grid[row][col] = 2
                        queue.append((row, col))
                        fresh -= 1
            time += 1

        return time if fresh == 0 else -1
