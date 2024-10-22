# https://leetcode.com/problems/harshad-number/description/


class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        sum_digits = sum(map(int, str(x)))
        if x % sum_digits == 0:
            return sum_digits
        else:
            return -1
