# https://leetcode.com/problems/palindrome-number/description/


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        temp = x
        num = 0
        while temp != 0:
            digit = temp % 10
            num = num * 10 + digit
            temp //= 10
        return x == num
