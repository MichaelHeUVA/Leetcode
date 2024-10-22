# https://leetcode.com/problems/summary-ranges/description/
from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        output = []
        start = 0
        for i, num in enumerate(nums):
            if i == len(nums) - 1:
                if nums[i - 1] + 1 == num:
                    output.append(f"{nums[start]}->{num}")
                else:
                    output.append(f"{num}")
            elif i < len(nums) - 1 and nums[i + 1] - 1 != num:
                if start == i:
                    output.append(f"{num}")
                else:
                    output.append(f"{nums[start]}->{num}")
                start = i + 1
        return output
