# https://leetcode.com/problems/reverse-substrings-between-each-pair-of-parentheses/description/


class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        for char in s:
            if char == ")":
                temp = []
                while stack[-1] != "(":
                    temp.append(stack.pop())
                stack.pop()
                for i in range(len(temp)):
                    stack.append(temp[i])
            else:
                stack.append(char)
        return "".join(stack)
