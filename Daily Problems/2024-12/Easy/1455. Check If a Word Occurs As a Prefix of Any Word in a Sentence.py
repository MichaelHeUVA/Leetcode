# https://leetcode.com/problems/check-if-a-word-occurs-as-a-prefix-of-any-word-in-a-sentence/description/?envType=daily-question&envId=2024-12-02


class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        words = sentence.split()
        print(words)
        for i, word in enumerate(words):
            if len(searchWord) <= len(word) and word[: len(searchWord)] == searchWord:
                return i + 1
        return -1
