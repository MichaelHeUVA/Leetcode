# https://leetcode.com/problems/remove-sub-folders-from-the-filesystem/description/?envType=daily-question&envId=2024-10-25
from typing import List


class TrieNode:
    def __init__(self):
        self.children = {}
        self.terminal = False

    def insert(self, word):
        current_node = self
        for char in word:
            if current_node.terminal:
                return False
            if char not in current_node.children:
                current_node.children[char] = TrieNode()
            current_node = current_node.children[char]
        current_node.terminal = True
        return True


class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()
        root = TrieNode()
        output = []
        for fold in folder:
            if root.insert(fold.split("/")):
                output.append(fold)
        return output
