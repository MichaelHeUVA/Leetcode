# https://leetcode.com/problems/largest-combination-with-bitwise-and-greater-than-zero/?envType=daily-question&envId=2024-11-07
from typing import List


class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        max_count = 0
        for i in range(24):
            count = 0
            for num in candidates:
                if num & (1 << i):
                    count += 1
            max_count = max(max_count, count)
        return max_count
