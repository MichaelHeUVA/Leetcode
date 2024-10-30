# https://leetcode.com/problems/determine-if-two-strings-are-close/description/
from collections import Counter


class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        count1 = Counter(word1)
        count2 = Counter(word2)
        for key in count1:
            if key not in count2:
                return False
        for key in count2:
            if key not in count1:
                return False
        if sorted(count1.values()) != sorted(count2.values()):
            return False
        return True
