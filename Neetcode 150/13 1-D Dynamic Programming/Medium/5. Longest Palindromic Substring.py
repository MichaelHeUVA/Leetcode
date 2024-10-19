# https://leetcode.com/problems/longest-palindromic-substring/description/


class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_string = ""
        for i in range(len(s)):
            # odd case where palindrone starts from middle j = 0
            # even case where palindrone start from the middle two characters j = 1 where left, right = i, i + 1
            for j in [0, 1]:
                left, right = i, i + j
                while left >= 0 and right < len(s) and s[left] == s[right]:
                    window_size = right - left + 1
                    if window_size > len(max_string):
                        max_string = s[left : right + 1]
                    left -= 1
                    right += 1
        return max_string
