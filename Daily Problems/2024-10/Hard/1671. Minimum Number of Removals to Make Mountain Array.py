# https://leetcode.com/problems/minimum-number-of-removals-to-make-mountain-array/description/?envType=daily-question&envId=2024-10-30
from typing import List


class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        lis = [1] * len(nums)
        n = len(nums)
        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    lis[i] = max(lis[i], lis[j] + 1)
        lds = [1] * len(nums)
        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                if nums[j] < nums[i]:
                    lds[i] = max(lds[i], lds[j] + 1)

        min_removals = float("inf")
        for i in range(n):
            if lis[i] > 1 and lds[i] > 1:
                min_removals = min(min_removals, n - (lis[i] + lds[i] - 1))
        return min_removals
