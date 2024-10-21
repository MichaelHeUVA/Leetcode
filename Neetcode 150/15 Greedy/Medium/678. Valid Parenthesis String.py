# https://leetcode.com/problems/valid-parenthesis-string/description/


class Solution:
    def checkValidString(self, s: str) -> bool:
        left_parenthesis_min = left_parenthesis_max = 0
        for c in s:
            if c == "(":
                left_parenthesis_min += 1
                left_parenthesis_max += 1
            elif c == ")":
                left_parenthesis_min -= 1
                left_parenthesis_max -= 1
            else:
                left_parenthesis_min -= 1
                left_parenthesis_max += 1
            if left_parenthesis_min < 0:
                left_parenthesis_min = 0
            if left_parenthesis_max < 0:
                return False
        return left_parenthesis_min == 0
