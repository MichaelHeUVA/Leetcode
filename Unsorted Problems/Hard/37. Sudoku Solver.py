# https://leetcode.com/problems/sudoku-solver/description/
from typing import List


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        def validNumber(row, col, k):
            for i in range(9):
                if board[i][col] == k or board[row][i] == k:
                    return False

                subgrid_row = 3 * (row // 3) + i // 3
                subgrid_col = 3 * (col // 3) + i % 3
                if board[subgrid_row][subgrid_col] == k:
                    return False

            return True

        def backtrack(row, col):
            if row == 9:
                return True

            if col == 9:
                return backtrack(row + 1, 0)

            if board[row][col] == ".":
                for k in range(1, 10):
                    if validNumber(row, col, str(k)):
                        board[row][col] = str(k)

                        if backtrack(row, col + 1):
                            return True

                        board[row][col] = "."

                return False
            return backtrack(row, col + 1)

        backtrack(0, 0)

        return
