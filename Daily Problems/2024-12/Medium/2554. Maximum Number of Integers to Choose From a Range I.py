# https://leetcode.com/problems/maximum-number-of-integers-to-choose-from-a-range-i/description/?envType=daily-question&envId=2024-12-06
from typing import List


class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        banned = set(banned)
        num_sum = 0
        output = 0

        for num in range(1, n + 1):
            if num in banned:
                continue
            num_sum += num
            if num_sum <= maxSum:
                output += 1
        return output
