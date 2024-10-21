# https://leetcode.com/problems/jump-game-ii/description/
from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        result = 0
        left = 0
        right = 0
        while right < len(nums) - 1:
            max_distance = 0
            for i in range(left, right + 1):
                max_distance = max(max_distance, nums[i] + i)
            result += 1
            left = right + 1
            right = max_distance

        return result
