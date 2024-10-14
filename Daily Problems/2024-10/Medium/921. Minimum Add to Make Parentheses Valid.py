# https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/description/?envType=daily-question&envId=2024-10-09


class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        output = 0
        stack = 0
        for char in s:
            if char == "(":
                stack += 1
            elif char == ")":
                if stack == 0:
                    output += 1
                else:
                    stack -= 1

        return stack + output
