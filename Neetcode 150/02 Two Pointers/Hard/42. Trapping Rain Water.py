# https://leetcode.com/problems/trapping-rain-water/description/
from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        output = 0
        left = 0
        right = len(height) - 1
        left_greatest = 0
        right_greatest = 0

        while left <= right:
            if height[left] > height[right]:
                if right_greatest < height[right]:
                    right_greatest = height[right]
                elif right_greatest > height[right]:
                    output += right_greatest - height[right]
                right -= 1
            else:
                if left_greatest < height[left]:
                    left_greatest = height[left]
                elif left_greatest > height[left]:
                    output += left_greatest - height[left]
                left += 1

        return output
