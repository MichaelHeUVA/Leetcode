# https://leetcode.com/problems/contains-duplicate-ii/description/
from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = set()
        n = len(nums)
        for i in range(n):
            if nums[i] in window:
                return True
            window.add(nums[i])
            if len(window) > k:
                window.remove(nums[i - k])
        return False
