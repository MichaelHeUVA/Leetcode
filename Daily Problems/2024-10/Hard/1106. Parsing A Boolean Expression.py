# https://leetcode.com/problems/parsing-a-boolean-expression/description/


class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        def evaluate(operation, values):
            if operation == "!":
                return "f" if values[0] == "t" else "t"

            if operation == "&":
                for value in values:
                    if value == "f":
                        return "f"
                return "t"

            if operation == "|":
                for value in values:
                    if value == "t":
                        return "t"
                return "f"

        stack = []
        for char in expression:
            if char == ")":
                values = []
                while stack[-1] != "(":
                    values.append(stack.pop())
                stack.pop()
                operation = stack.pop()
                result = evaluate(operation, values)
                stack.append(result)
            elif char != ",":
                stack.append(char)

        return stack[-1] == "t"
