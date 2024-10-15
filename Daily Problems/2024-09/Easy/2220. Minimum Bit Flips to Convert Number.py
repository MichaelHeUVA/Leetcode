# https://leetcode.com/problems/minimum-bit-flips-to-convert-number/description/?envType=daily-question&envId=2024-09-11


class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        xor = start ^ goal
        output = 0
        while xor:
            output += xor & 1
            xor >>= 1
        return output
