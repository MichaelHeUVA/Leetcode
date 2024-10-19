# https://leetcode.com/problems/minimum-number-of-increments-on-subarrays-to-form-a-target-array/description/
from typing import List


class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        output = 0
        prev_val = 0
        for i in range(len(target)):
            if target[i] > prev_val:
                output += target[i] - prev_val
            prev_val = target[i]
        return output
