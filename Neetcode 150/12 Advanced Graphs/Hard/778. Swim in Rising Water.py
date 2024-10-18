# https://leetcode.com/problems/swim-in-rising-water/description/
from collections import deque
from heapq import heappop, heappush
from typing import List


# Binary search for time and see if we can reach the end
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        # do binary search for time and do dijikstras to see if we can reach the end
        rows = len(grid)
        cols = len(grid[0])

        # return true if we can get to the end
        def bfs(time):
            q = deque([(0, 0)])
            visited = set()
            visited.add(grid[0][0])

            if time < grid[0][0]:
                return False

            while q:
                size = len(q)
                for _ in range(size):
                    row, col = q.popleft()
                    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
                    for dx, dy in directions:
                        if (
                            row + dy >= rows
                            or col + dx >= cols
                            or row + dy < 0
                            or col + dx < 0
                            or grid[row + dy][col + dx] in visited
                            or grid[row + dy][col + dx] > time
                        ):
                            continue
                        visited.add(grid[row + dy][col + dx])
                        q.append((row + dy, col + dx))
            if grid[rows - 1][cols - 1] in visited:
                return True
            return False

        # find max time
        right = 0
        for row in range(rows):
            for col in range(cols):
                right = max(right, grid[row][col])
        left = 0
        k = right
        while left <= right:
            mid = (left + right) // 2
            if bfs(mid):
                right = mid - 1
                k = mid
            else:
                left = mid + 1

        return k


# Dijikstras algorithm
class Solution:  # noqa F811
    def swimInWater(self, grid: List[List[int]]) -> int:
        h = [(grid[0][0], 0, 0)]
        visited = {(0, 0)}

        d = [
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1),
        ]

        while h:
            score, x, y = heappop(h)
            x, y = -x, -y

            for dx, dy in d:
                new_x = x + dx
                new_y = y + dy
                if (
                    0 <= new_x < len(grid)
                    and 0 <= new_y < len(grid)
                    and (new_x, new_y) not in visited
                ):
                    visited.add((new_x, new_y))
                    if new_x == len(grid) - 1 and new_y == len(grid) - 1:
                        return max(score, grid[-1][-1])
                    heappush(h, (max(score, grid[new_x][new_y]), -new_x, -new_y))

        return 0
