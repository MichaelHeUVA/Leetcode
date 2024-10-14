# https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses/description/?envType=daily-question&envId=2024-04-04


class Solution:
    def maxDepth(self, s: str) -> int:
        stack = 0
        max_nest = 0
        for character in s:
            if character == "(":
                stack += 1
                max_nest = max(max_nest, stack)
            elif character == ")":
                stack -= 1
        return max_nest
