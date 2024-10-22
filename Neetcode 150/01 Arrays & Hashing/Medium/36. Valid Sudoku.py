# https://leetcode.com/problems/valid-sudoku/description/
from collections import defaultdict
from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows, cols = len(board), len(board[0])
        row_nums = defaultdict(set)
        col_nums = defaultdict(set)
        square_nums = defaultdict(set)
        for row in range(rows):
            for col in range(cols):
                num = board[row][col]
                if num != ".":
                    if (
                        num in row_nums[row]
                        or num in col_nums[col]
                        or num in square_nums[(row // 3, col // 3)]
                    ):
                        return False
                    row_nums[row].add(num)
                    col_nums[col].add(num)
                    square_nums[(row // 3, col // 3)].add(num)

        return True
