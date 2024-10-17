# https://leetcode.com/problems/implement-trie-prefix-tree/description/


class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        current_node = self.root

        for char in word:
            if char not in current_node.children:
                current_node.children[char] = Node()
            current_node = current_node.children[char]
        current_node.terminal = True

    def search(self, word: str) -> bool:
        current_node = self.find(word)
        return current_node is not None and current_node.terminal

    def startsWith(self, prefix: str) -> bool:
        return self.find(prefix) is not None

    def find(self, word: str):
        current_node = self.root
        for char in word:
            if char not in current_node.children:
                return None
            current_node = current_node.children[char]
        return current_node


class Node:
    def __init__(self, terminal=False):
        self.terminal = terminal
        self.children = {}


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
