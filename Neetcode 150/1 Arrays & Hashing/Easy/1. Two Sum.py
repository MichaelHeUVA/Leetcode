# https://leetcode.com/problems/two-sum/description/
from collections import defaultdict
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        m = defaultdict(int)
        for i in range(len(nums)):
            if target - nums[i] in m:
                return [m[target - nums[i]], i]
            m[nums[i]] = i
        return []
