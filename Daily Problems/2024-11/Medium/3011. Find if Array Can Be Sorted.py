# https://leetcode.com/problems/find-if-array-can-be-sorted/description/?envType=daily-question&envId=2024-11-06
from typing import List


class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        if nums == sorted(nums):
            return True
        prev_set_bits = 0
        prev_max = float("-inf")
        curr_min = float("inf")
        curr_max = float("-inf")
        for i in range(len(nums)):
            if prev_set_bits != bin(nums[i]).count("1"):
                prev_max = curr_max
                curr_max = float("-inf")
                curr_min = float("inf")
                prev_set_bits = bin(nums[i]).count("1")

            curr_max = max(curr_max, nums[i])
            curr_min = min(curr_min, nums[i])
            if prev_max > curr_min:
                return False
        return True
