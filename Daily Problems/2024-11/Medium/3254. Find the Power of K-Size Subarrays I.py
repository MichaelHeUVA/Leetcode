# https://leetcode.com/problems/find-the-power-of-k-size-subarrays-i/description/?envType=daily-question&envId=2024-11-16
from typing import List


class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        if k == 1:
            return nums
        n = len(nums)
        output = [-1] * (n - k + 1)
        consecutive_count = 1
        for i in range(n - 1):
            if nums[i] + 1 == nums[i + 1]:
                consecutive_count += 1
            else:
                consecutive_count = 1
            if consecutive_count >= k:
                output[(i + 1) - k + 1] = nums[i + 1]
        return output
