# https://leetcode.com/problems/valid-parentheses/description/


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char == "(" or char == "[" or char == "{":
                stack.append(char)
            else:
                if stack:
                    if (
                        stack[-1] == "("
                        and char == ")"
                        or stack[-1] == "["
                        and char == "]"
                        or stack[-1] == "{"
                        and char == "}"
                    ):
                        stack.pop()
                    else:
                        return False
                else:
                    return False
        return len(stack) == 0
