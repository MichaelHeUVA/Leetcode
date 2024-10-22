# https://leetcode.com/problems/word-search/description/
from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(index, i, j):
            if (
                i < 0
                or i >= len(board[0])
                or j < 0
                or j >= len(board)
                or board[j][i] == 1
            ):
                return False
            result = False
            original = board[j][i]
            if word[index] == board[j][i]:
                board[j][i] = 1
                if index + 1 == len(word):
                    return True
                else:
                    result = (
                        result
                        or dfs(index + 1, i - 1, j)
                        or dfs(index + 1, i + 1, j)
                        or dfs(index + 1, i, j - 1)
                        or dfs(index + 1, i, j + 1)
                    )
            board[j][i] = original
            return result

        for i in range(len(board[0])):
            for j in range(len(board)):
                if dfs(0, i, j):
                    return True
        return False
