# https://leetcode.com/problems/target-sum/description/
from collections import defaultdict
from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = defaultdict(int)

        def backtrack(index, total):
            if total == target and index == len(nums):
                return 1
            if index + 1 > len(nums):
                return 0
            if (index, total) in dp:
                return dp[(index, total)]
            dp[(index, total)] = backtrack(index + 1, total + nums[index]) + backtrack(
                index + 1, total - nums[index]
            )
            return dp[(index, total)]

        return backtrack(0, 0)
