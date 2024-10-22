# https://leetcode.com/problems/beautiful-towers-i/description/
from typing import List


class Solution:
    def maximumSumOfHeights(self, heights: List[int]) -> int:
        total = sum(heights)
        min_removals = float("inf")
        for i in range(len(heights)):
            removals = 0
            prev = heights[i]
            for j in range(i - 1, -1, -1):
                if heights[j] > prev:
                    removals += heights[j] - prev
                else:
                    prev = heights[j]
            prev = heights[i]
            for j in range(i + 1, len(heights)):
                if heights[j] > prev:
                    removals += heights[j] - prev
                else:
                    prev = heights[j]

            min_removals = min(min_removals, removals)
        return total - min_removals
