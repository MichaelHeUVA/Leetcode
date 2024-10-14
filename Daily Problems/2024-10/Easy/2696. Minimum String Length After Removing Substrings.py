# https://leetcode.com/problems/minimum-string-length-after-removing-substrings/description/?envType=daily-question&envId=2024-10-07


class Solution:
    def minLength(self, s: str) -> int:
        stack = []
        for char in s:
            if stack and char == "B" and stack[-1] == "A":
                stack.pop()
            elif stack and char == "D" and stack[-1] == "C":
                stack.pop()
            else:
                stack.append(char)
        return len(stack)
