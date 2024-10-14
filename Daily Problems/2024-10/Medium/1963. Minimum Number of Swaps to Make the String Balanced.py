# https://leetcode.com/problems/minimum-number-of-swaps-to-make-the-string-balanced/description/?envType=daily-question&envId=2024-10-08


class Solution:
    def minSwaps(self, s: str) -> int:
        stack = 0
        count = 0
        for char in s:
            if char == "[":
                stack += 1
            elif char == "]":
                if stack > 0:
                    stack -= 1
                else:
                    stack += 1
                    count += 1

        return count
