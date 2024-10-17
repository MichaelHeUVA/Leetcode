# https://leetcode.com/problems/n-queens/description/
from typing import List


# Optimized
class Solution:
    def totalNQueens(self, n: int) -> int:
        col_set = set()
        row_set = set()
        diag_set = set()
        anti_diag_set = set()
        self.output = 0

        def backtrack(row):
            if row == n:
                self.output += 1
                return

            for col in range(n):
                if (
                    col in col_set
                    or row in row_set
                    or (row - col) in diag_set
                    or (row + col) in anti_diag_set
                ):
                    continue
                col_set.add(col)
                row_set.add(row)
                diag_set.add((row - col))
                anti_diag_set.add((row + col))

                backtrack(row + 1)

                col_set.remove(col)
                row_set.remove(row)
                diag_set.remove((row - col))
                anti_diag_set.remove((row + col))

        backtrack(0)
        return self.output


# First attempt
class Solution:  # noqa: F811
    def solveNQueens(self, n: int) -> List[List[str]]:
        output = []

        def canPlaceQueen(row, col, board):
            if board[row][col] == "Q":
                return False

            for i in range(n):
                if i != row and board[i][col] == "Q":
                    return False
            for i in range(n):
                if i != col and board[row][i] == "Q":
                    return False

            # Check diagonals
            i = row
            j = col
            while i >= 0 and j >= 0:
                if i != row and j != col and board[i][j] == "Q":
                    return False
                i -= 1
                j -= 1
            i = row
            j = col
            while i < n and j < n:
                if i != row and j != col and board[i][j] == "Q":
                    return False
                i += 1
                j += 1
            i = row
            j = col
            while i >= 0 and j >= 0 and i < n and j < n:
                if i != row and j != col and board[i][j] == "Q":
                    return False
                i += 1
                j -= 1
            i = row
            j = col
            while i >= 0 and j >= 0 and i < n and j < n:
                if i != row and j != col and board[i][j] == "Q":
                    return False
                i -= 1
                j += 1
            return True

        def placeQueen(row, col, board):
            return board[row][:col] + "Q" + board[row][col + 1 :]

        def removeQueen(row, col, board):
            return board[row][:col] + "." + board[row][col + 1 :]

        def backtrack(row, board, queens):
            if queens == n:
                output.append(board[::])
                return

            for col in range(n):
                if canPlaceQueen(row, col, board):
                    print(board)
                    print(queens)
                    board[row] = placeQueen(row, col, board)
                    backtrack(row + 1, board, queens + 1)
                    board[row] = removeQueen(row, col, board)

        row_string = ""
        for _ in range(n):
            row_string += "."
        board = [row_string for _ in range(n)]
        backtrack(0, board, 0)

        return output
