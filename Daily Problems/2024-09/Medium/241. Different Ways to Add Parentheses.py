# https://leetcode.com/problems/different-ways-to-add-parentheses/description/?envType=daily-question&envId=2024-09-19
from typing import List


class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        output = []
        if len(expression) == 0:
            return []

        if len(expression) == 1:
            return [int(expression)]

        if len(expression) == 2 and expression[0].isdigit():
            return [int(expression)]

        for i, char in enumerate(expression):
            if char.isdigit():
                continue

            left_ways = self.diffWaysToCompute(expression[:i])
            right_ways = self.diffWaysToCompute(expression[i + 1 :])

            for left in left_ways:
                for right in right_ways:
                    if char == "+":
                        output.append(left + right)
                    elif char == "-":
                        output.append(left - right)
                    elif char == "*":
                        output.append(left * right)

        return output
