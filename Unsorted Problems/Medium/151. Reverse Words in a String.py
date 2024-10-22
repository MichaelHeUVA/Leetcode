# https://leetcode.com/problems/reverse-words-in-a-string/description/


class Solution:
    def reverseWords(self, s: str) -> str:
        string = s.split()
        left = 0
        right = len(string) - 1
        while left < right:
            string[left], string[right] = string[right], string[left]
            left += 1
            right -= 1
        return " ".join(string)
