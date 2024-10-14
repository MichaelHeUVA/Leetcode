# https://leetcode.com/problems/maximum-width-ramp/description/?envType=daily-question&envId=2024-10-10


class Solution:
    def maxWidthRamp(self, nums):
        n = len(nums)
        mono_stack = []  # monotonically decreasing stack

        for i in range(n):
            if not mono_stack or nums[mono_stack[-1]] >= nums[i]:
                mono_stack.append(i)

        max_width = 0
        for i in range(n - 1, -1, -1):
            while mono_stack and nums[mono_stack[-1]] <= nums[i]:
                max_width = max(max_width, i - mono_stack.pop())

        return max_width
