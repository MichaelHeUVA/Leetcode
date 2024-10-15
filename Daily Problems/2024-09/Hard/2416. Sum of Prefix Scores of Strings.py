# https://leetcode.com/problems/sum-of-prefix-scores-of-strings/description/?envType=daily-question&envId=2024-09-25
from typing import List


class TrieNode:
    def __init__(self):
        self.children = {}
        self.count = 0  # count of how many there are
        self.terminal = False

    def addWord(self, word):
        current_node = self
        for char in word:
            if char not in current_node.children:
                current_node.children[char] = TrieNode()
            current_node = current_node.children[char]
            current_node.count += 1
        current_node.terminal = True

    def countPrefixes(self, word):
        score = 0
        current_node = self
        for char in word:
            score += current_node.children[char].count
            current_node = current_node.children[char]
        return score

    # def __str__(self):
    #     return str(self.children) + str(self.count)


class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        # trie with count at the terminal node?
        root = TrieNode()
        for word in words:
            root.addWord(word)
        output = []
        for word in words:
            output.append(root.countPrefixes(word))
        return output
