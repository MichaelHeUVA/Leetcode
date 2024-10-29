# https://leetcode.com/problems/divide-two-integers/description/


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == 0:
            return 0
        if dividend == -2147483648 and divisor == -1:
            return 2147483647
        if (dividend < 0) != (divisor < 0):
            negative = True
        else:
            negative = False
        dividend = abs(dividend)
        divisor = abs(divisor)
        count = 0
        while dividend >= divisor:
            power_of_two = 1
            value = divisor
            while value <= (dividend >> 1):
                value <<= 1
                power_of_two <<= 1
            count += power_of_two
            dividend -= value
        return -count if negative else count
