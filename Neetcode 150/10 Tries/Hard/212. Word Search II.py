# https://leetcode.com/problems/word-search-ii/description/
from typing import List


class TrieNode:
    def __init__(self):
        self.children = {}
        self.terminal = False

    def addWord(self, word):
        current_node = self

        for char in word:
            if char not in current_node.children:
                current_node.children[char] = TrieNode()
            current_node = current_node.children[char]
        current_node.terminal = True


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for word in words:
            root.addWord(word)

        rows = len(board)
        cols = len(board[0])

        result = set()
        visited = set()

        def dfs(row, col, node, word):
            if (
                row < 0
                or col < 0
                or row >= rows
                or col >= cols
                or (row, col) in visited
                or board[row][col] not in node.children
            ):
                return
            visited.add((row, col))
            node = node.children[board[row][col]]
            word += board[row][col]
            if node.terminal:
                result.add(word)

            dfs(row + 1, col, node, word)
            dfs(row - 1, col, node, word)
            dfs(row, col + 1, node, word)
            dfs(row, col - 1, node, word)

            visited.remove((row, col))
            return

        for row in range(rows):
            for col in range(cols):
                dfs(row, col, root, "")

        return list(result)
