# https://leetcode.com/problems/longest-palindrome-by-concatenating-two-letter-words/description/
from collections import defaultdict
from typing import List


class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        word_map = defaultdict(int)
        for word in words:
            word_map[word] += 1
        longest_palindrome = 0
        double_letter_used = False
        for word in words:
            if word == word[::-1]:
                if word_map[word] > 1:
                    longest_palindrome += 4
                    word_map[word] -= 2
                elif word_map[word] == 1 and not double_letter_used:
                    double_letter_used = True
                    longest_palindrome += 2
            elif word_map[word] > 0 and word_map[word[::-1]] > 0:
                longest_palindrome += 4
                word_map[word] -= 1
                word_map[word[::-1]] -= 1
        return longest_palindrome
