# https://leetcode.com/problems/implement-trie-ii-prefix-tree/description/


class Trie:
    def __init__(self):
        self.children = {}
        self.count = 0
        self.terminal = 0

    def insert(self, word: str) -> None:
        current_node = self
        for char in word:
            if char not in current_node.children:
                current_node.children[char] = Trie()
            current_node = current_node.children[char]
            current_node.count += 1
        current_node.terminal += 1
        return

    def countWordsEqualTo(self, word: str) -> int:
        current_node = self
        for char in word:
            if char not in current_node.children:
                return 0
            current_node = current_node.children[char]
        if current_node.terminal > 0:
            return current_node.terminal
        return 0

    def countWordsStartingWith(self, prefix: str) -> int:
        current_node = self
        for char in prefix:
            if char not in current_node.children:
                return 0
            current_node = current_node.children[char]
        return current_node.count

    def erase(self, word: str) -> None:
        current_node = self
        for char in word:
            current_node = current_node.children[char]
            current_node.count -= 1
        current_node.terminal -= 1
        return


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.countWordsEqualTo(word)
# param_3 = obj.countWordsStartingWith(prefix)
# obj.erase(word)
