# https://leetcode.com/problems/subarray-sum-equals-k/description/
from collections import defaultdict
from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        counts = defaultdict(int)
        subarrays = 0
        current_sum = 0
        for num in nums:
            current_sum += num

            if current_sum == k:
                subarrays += 1

            subarrays += counts[current_sum - k]

            counts[current_sum] += 1

        return subarrays
