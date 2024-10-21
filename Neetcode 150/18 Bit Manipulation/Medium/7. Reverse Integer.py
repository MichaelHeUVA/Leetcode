# https://leetcode.com/problems/reverse-integer/description/


class Solution:
    def reverse(self, x: int) -> int:
        negative = False
        if x < 0:
            negative = True
            x = -x
        reversed = 0
        while x != 0:
            reversed *= 10
            reversed += x % 10
            x = x // 10
        if reversed <= -pow(2, 31) or reversed >= pow(2, 31):
            return 0
        if negative:
            return -reversed
        return reversed
