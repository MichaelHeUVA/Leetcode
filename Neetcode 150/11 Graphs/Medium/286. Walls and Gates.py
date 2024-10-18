# https://leetcode.com/problems/walls-and-gates/description/
from collections import deque
from typing import List


class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        rows = len(rooms)
        cols = len(rooms[0])

        q = deque()
        for row in range(rows):
            for col in range(cols):
                if rooms[row][col] == 0:
                    q.append((row, col))

        while q:
            size = len(q)
            for _ in range(size):
                row, col = q.popleft()
                directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
                for dx, dy in directions:
                    if (
                        row + dy >= rows
                        or col + dx >= cols
                        or row + dy < 0
                        or col + dx < 0
                        or rooms[row + dy][col + dx] != 2147483647
                    ):
                        continue
                    rooms[row + dy][col + dx] = rooms[row][col] + 1
                    q.append((row + dy, col + dx))

        return
