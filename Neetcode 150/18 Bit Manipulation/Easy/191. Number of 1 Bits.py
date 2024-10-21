# https://leetcode.com/problems/number-of-1-bits/description/


class Solution:
    def hammingWeight(self, n: int) -> int:
        output = 0
        while n:
            output += 1 & n
            n //= 2
        return output
