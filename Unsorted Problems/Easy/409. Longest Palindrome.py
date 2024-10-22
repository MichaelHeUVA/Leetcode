# https://leetcode.com/problems/longest-palindrome/description/
from collections import Counter


class Solution:
    def longestPalindrome(self, s: str) -> int:
        counts = Counter(s)
        center = False
        output = 0
        for char, count in counts.items():
            if count == 1:
                if not center:
                    center = True
                    output += 1
            else:
                if count % 2 == 0:
                    output += count
                else:
                    output += count - 1
                    if not center:
                        center = True
                        output += 1
        return output
