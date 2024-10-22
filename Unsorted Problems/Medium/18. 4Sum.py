# https://leetcode.com/problems/4sum/description/
from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        output = []
        for a in range(len(nums)):
            if a > 0 and nums[a] == nums[a - 1]:
                continue
            for b in range(a + 1, len(nums)):
                if b > a + 1 and nums[b] == nums[b - 1]:
                    continue
                c = b + 1
                d = len(nums) - 1
                while c < d:
                    s = nums[a] + nums[b] + nums[c] + nums[d]
                    if s > target:
                        d -= 1
                    elif s < target:
                        c += 1
                    else:
                        output.append([nums[a], nums[b], nums[c], nums[d]])
                        c += 1
                        while nums[c] == nums[c - 1] and c < d:
                            c += 1
        return output
