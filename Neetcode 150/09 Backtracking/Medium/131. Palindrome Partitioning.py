# https://leetcode.com/problems/palindrome-partitioning/description/
from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        output = []

        def backtrack(start, path):
            if start >= len(s):
                output.append(path.copy())
                return
            for end in range(start, len(s)):
                if self.isPalindrome(s[start : end + 1]):
                    path.append(s[start : end + 1])
                    backtrack(end + 1, path)
                    path.pop()

        backtrack(0, [])
        return output

    def isPalindrome(self, s):
        left = 0
        right = len(s) - 1
        while left <= right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1

        return True
