# https://leetcode.com/problems/majority-element/description/
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority = 0
        count = 0

        for num in nums:
            if count == 0:
                majority = num

            if num == majority:
                count += 1
            else:
                count -= 1

        return majority
