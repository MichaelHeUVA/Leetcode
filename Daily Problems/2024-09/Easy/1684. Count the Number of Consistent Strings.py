# https://leetcode.com/problems/count-the-number-of-consistent-strings/description/?envType=daily-question&envId=2024-09-12
from typing import List


class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        good = set(allowed)
        output = 0
        for word in words:
            good_word = True
            for char in word:
                if char not in good:
                    good_word = False
            output += good_word
        return output
