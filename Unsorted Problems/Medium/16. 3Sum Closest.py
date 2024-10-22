# https://leetcode.com/problems/3sum-closest/description/
from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        dist = float("inf")
        output = 0
        for a in range(len(nums)):
            b = a + 1
            c = len(nums) - 1
            while b < c:
                s = nums[a] + nums[b] + nums[c]
                if dist > abs(s - target):
                    dist = abs(s - target)
                    output = s
                if s > target:
                    c -= 1
                elif s < target:
                    b += 1
                else:
                    return s
        return output
