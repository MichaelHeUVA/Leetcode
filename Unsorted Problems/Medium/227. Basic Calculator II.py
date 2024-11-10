# https://leetcode.com/problems/basic-calculator-ii/description/


class Solution:
    def calculate(self, s: str) -> int:
        def get_number():
            nonlocal i
            number = int(s[i])
            while i + 1 < len(s) and s[i + 1].isnumeric():
                number *= 10
                number += int(s[i + 1])
                i += 1
            return number

        stack = []
        s = s.replace(" ", "")
        i = 0
        while i < len(s):
            if s[i].isnumeric():
                number = get_number()
                stack.append(number)
            elif s[i] == "*":
                num1 = int(stack.pop())
                i += 1
                num2 = get_number()
                stack.append(num1 * num2)
            elif s[i] == "/":
                num1 = int(stack.pop())
                i += 1
                num2 = get_number()
                stack.append(num1 // num2)
            else:
                stack.append(s[i])
            i += 1

        add_sub = stack
        i = 0
        stack = []
        while i < len(add_sub):
            if type(add_sub[i]) is int:
                stack.append(add_sub[i])
            elif add_sub[i] == "+":
                stack.append(stack.pop() + add_sub[i + 1])
                i += 1
            else:
                stack.append(stack.pop() - add_sub[i + 1])
                i += 1
            i += 1
        return stack[0]
