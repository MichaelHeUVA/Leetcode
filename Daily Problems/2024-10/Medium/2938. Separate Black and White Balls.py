# https://leetcode.com/problems/separate-black-and-white-balls/description/?envType=daily-question&envId=2024-10-15


class Solution:
    def minimumSteps(self, s: str) -> int:
        k = 0
        swaps = 0
        for i in range(len(s)):
            if s[i] == "0":
                swaps += i - k
                k += 1

        return swaps
