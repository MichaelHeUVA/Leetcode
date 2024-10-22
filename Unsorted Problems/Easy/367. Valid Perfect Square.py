# https://leetcode.com/problems/valid-perfect-square/description/


class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        left = 0
        right = num
        while left <= right:
            mid = (left + right) // 2
            if mid * mid == num:
                return True
            elif mid * mid < num:
                left = mid + 1
            elif mid * mid > num:
                right = mid - 1
        return False
