# https://leetcode.com/problems/max-number-of-k-sum-pairs/description/
from collections import defaultdict
from typing import List


class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        m = defaultdict(int)
        output = 0
        for i in range(len(nums)):
            complement = k - nums[i]
            if m[complement] > 0:
                m[complement] -= 1
                output += 1
            else:
                m[nums[i]] += 1
        return output
