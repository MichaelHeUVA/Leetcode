# https://leetcode.com/problems/generate-parentheses/description/
from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def backtrack(open_parentheses, close_parentheses, path):
            if open_parentheses == close_parentheses == n:
                result.append(path)
                return

            if open_parentheses < n:
                backtrack(open_parentheses + 1, close_parentheses, path + "(")

            if close_parentheses < open_parentheses:
                backtrack(open_parentheses, close_parentheses + 1, path + ")")

        backtrack(0, 0, "")
        return result
