# https://leetcode.com/problems/partition-equal-subset-sum/description/
from typing import List
from copy import copy


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False
        subset_sum = sum(nums) / 2
        dp = set()
        for num in nums:
            deep_dp = copy.deepcopy(dp)
            deep_dp.add(num)
            for numbers in dp:
                deep_dp.add(numbers + num)
            dp = deep_dp
            if subset_sum in dp:
                return True
        return False
