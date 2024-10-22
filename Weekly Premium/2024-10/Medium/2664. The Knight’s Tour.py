# https://leetcode.com/problems/the-knights-tour/description/?envType=weekly-question&envId=2024-10-22
from typing import List


class Solution:
    def tourOfKnight(self, m: int, n: int, r: int, c: int) -> List[List[int]]:
        path = [[-1] * n for _ in range(m)]
        path[r][c] = 0
        moves = ((1, 2), (-1, 2), (1, -2), (-1, -2), (2, 1), (-2, 1), (2, -1), (-2, -1))

        def backtrack(row, col, count):
            if count == (m * n):
                return True
            for i, j in moves:
                if (
                    0 <= row + i < m
                    and 0 <= col + j < n
                    and path[row + i][col + j] == -1
                ):
                    path[row + i][col + j] = count
                    if backtrack(row + i, col + j, count + 1):
                        return True
                    path[row + i][col + j] = -1
            return False

        backtrack(r, c, 1)
        return path
