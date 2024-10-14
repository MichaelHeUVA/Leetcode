# https://leetcode.com/problems/longest-valid-parentheses/description/


# Two Pass
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        left = 0
        right = 0
        max_length = 0
        n = len(s)

        for i in range(n):
            if s[i] == "(":
                left += 1
            else:
                right += 1
            if left == right:
                max_length = max(max_length, left + right)
            elif right > left:
                left = 0
                right = 0

        left = 0
        right = 0

        for i in range(n - 1, -1, -1):
            if s[i] == "(":
                left += 1
            else:
                right += 1
            if left == right:
                max_length = max(max_length, left + right)
            elif left > right:
                left = 0
                right = 0

        return max_length


# Stack
class Solution:  # noqa: F811
    def longestValidParentheses(self, s: str) -> int:
        max_valid = 0
        stack = []
        stack.append(-1)
        for i, char in enumerate(s):
            if char == "(":
                stack.append(i)
            elif char == ")":
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    max_valid = max(max_valid, i - stack[-1])
        return max_valid
