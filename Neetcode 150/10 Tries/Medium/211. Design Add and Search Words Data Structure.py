# https://leetcode.com/problems/design-add-and-search-words-data-structure/description/


class WordDictionary:
    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        current_node = self.root

        for char in word:
            if char not in current_node.children:
                current_node.children[char] = Node()
            current_node = current_node.children[char]
        current_node.terminal = True

    def search(self, word: str) -> bool:
        def dfs(index, node):
            if index == len(word):
                return node.terminal
            if word[index] == ".":
                for child_node in node.children.values():
                    if dfs(index + 1, child_node):
                        return True
                return False
            else:
                if word[index] not in node.children:
                    return False
                return dfs(index + 1, node.children[word[index]])

        return dfs(0, self.root)


class Node:
    def __init__(self, terminal=False):
        self.terminal = terminal
        self.children = {}


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
