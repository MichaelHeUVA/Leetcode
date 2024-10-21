# https://leetcode.com/problems/jump-game/description/
from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        pointer = len(nums) - 1
        for i in range(len(nums) - 2, -1, -1):
            if i + nums[i] >= pointer:
                pointer = i
        return pointer == 0
