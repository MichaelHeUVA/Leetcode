# https://leetcode.com/problems/make-sum-divisible-by-p/description/?envType=daily-question&envId=2024-10-03
from typing import List


class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        s = sum(nums)
        if s % p == 0:
            return 0
        remainder = s % p
        mod_map = {0: -1}
        current_sum = 0
        min_length = len(nums)
        for i in range(len(nums)):
            current_sum = (current_sum + nums[i]) % p
            needed = (current_sum - remainder + p) % p
            if needed in mod_map:
                min_length = min(min_length, i - mod_map[needed])
            mod_map[current_sum] = i

        return -1 if min_length == len(nums) else min_length
