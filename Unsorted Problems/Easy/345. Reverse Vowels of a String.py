# https://leetcode.com/problems/reverse-vowels-of-a-string/description/


class Solution:
    def reverseVowels(self, s: str) -> str:
        left = 0
        right = len(s) - 1
        vowel = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}
        string = list(s)
        while left < right:
            while left < right and string[left] not in vowel:
                left += 1
            while left < right and string[right] not in vowel:
                right -= 1
            string[left], string[right] = string[right], string[left]
            left += 1
            right -= 1
        return "".join(string)
