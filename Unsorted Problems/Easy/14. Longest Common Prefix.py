# https://leetcode.com/problems/longest-common-prefix/description/
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

    def findLongestPrefix(self):
        current_node = self
        output = ""
        while len(current_node.children) == 1 and not current_node.terminal:
            output += list(current_node.children.keys())[0]
            current_node = current_node.children[list(current_node.children.keys())[0]]
        return output


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        root = TrieNode()
        for word in strs:
            root.addWord(word)
        return root.findLongestPrefix()
