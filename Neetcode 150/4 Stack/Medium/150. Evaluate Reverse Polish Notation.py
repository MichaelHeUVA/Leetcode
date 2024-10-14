# https://leetcode.com/problems/evaluate-reverse-polish-notation/description/
from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if not stack:
                stack.append(int(token))
            elif token == "+":
                b = stack.pop()
                a = stack.pop()
                stack.append(a + b)
            elif token == "-":
                b = stack.pop()
                a = stack.pop()
                stack.append(a - b)
            elif token == "*":
                b = stack.pop()
                a = stack.pop()
                stack.append(a * b)
            elif token == "/":
                b = stack.pop()
                a = stack.pop()
                stack.append(int(float(a) / float(b)))
            else:
                stack.append(int(token))

        return stack[-1]
