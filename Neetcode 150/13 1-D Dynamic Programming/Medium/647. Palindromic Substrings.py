# https://leetcode.com/problems/palindromic-substrings/description/


class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        for i in range(len(s)):
            # odd case where palindrone starts from middle j = 0
            # even case where palindrone start from the middle two characters j = 1 where left, right = i, i + 1
            for j in [0, 1]:
                left, right = i, i + j
                while left >= 0 and right < len(s) and s[left] == s[right]:
                    count += 1
                    left -= 1
                    right += 1
        return count
