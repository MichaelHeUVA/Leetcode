# https://leetcode.com/problems/01-matrix/description/
from collections import deque
from typing import List


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows = len(mat)
        cols = len(mat[0])
        q = deque()
        visited = set()
        for row in range(rows):
            for col in range(cols):
                if mat[row][col] == 0:
                    q.append((row, col, 0))
                    visited.add((row, col))
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        while q:
            size = len(q)
            for i in range(size):
                row, col, dist = q.popleft()
                for dx, dy in directions:
                    if (
                        row + dx >= 0
                        and col + dy >= 0
                        and row + dx < rows
                        and col + dy < cols
                        and (row + dx, col + dy) not in visited
                    ):
                        q.append((row + dx, col + dy, dist + 1))
                        visited.add((row + dx, col + dy))
                        mat[row + dx][col + dy] = dist + 1

        return mat
