# https://leetcode.com/problems/remove-k-digits/description/


class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for digit in num:
            while stack and digit < stack[-1] and k > 0:
                stack.pop()
                k -= 1
            stack.append(digit)

        while k > 0:
            stack.pop()
            k -= 1

        result = "".join(stack).lstrip("0")

        return result if result else "0"
