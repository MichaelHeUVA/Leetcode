# https://leetcode.com/problems/minimum-difference-between-largest-and-smallest-value-in-three-moves/description/
from typing import List
from heapq import nlargest, nsmallest


class Solution:
    def minDifference(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 4:
            return 0

        smallest_four = sorted(nsmallest(4, nums))
        largest_four = sorted(nlargest(4, nums))

        min_diff = float("inf")
        for i in range(4):
            min_diff = min(min_diff, largest_four[i] - smallest_four[i])
        return min_diff
