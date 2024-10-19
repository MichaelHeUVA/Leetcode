# https://leetcode.com/problems/house-robber-ii/
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        def houseRobber(nums):
            dp = [0] * len(nums)
            dp[0] = nums[0]
            dp[1] = max(nums[0], nums[1])
            for i in range(2, len(nums)):
                dp[i] = max(nums[i] + dp[i - 2], dp[i - 1])
            return dp[-1]

        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums)

        return max(houseRobber(nums[1:]), houseRobber(nums[:-1]))
