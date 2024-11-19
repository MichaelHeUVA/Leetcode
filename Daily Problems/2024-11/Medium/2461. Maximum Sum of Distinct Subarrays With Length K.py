# https://leetcode.com/problems/maximum-sum-of-distinct-subarrays-with-length-k/description/?envType=daily-question&envId=2024-11-19
from collections import Counter
from typing import List


class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        counts = Counter()
        unique_nums = 0
        window_sum = 0
        for i in range(k):
            if counts[nums[i]] == 0:
                unique_nums += 1
            counts[nums[i]] += 1
            window_sum += nums[i]
        output = 0
        if unique_nums == k:
            output = window_sum
        left = 0
        for right in range(k, n):
            counts[nums[left]] -= 1
            if counts[nums[left]] == 0:
                unique_nums -= 1
            window_sum -= nums[left]
            left += 1
            counts[nums[right]] += 1
            if counts[nums[right]] == 1:
                unique_nums += 1
            window_sum += nums[right]
            if unique_nums == k:
                output = max(output, window_sum)
        return output
