# https://leetcode.com/problems/largest-unique-number/description/
from collections import Counter
from typing import List


class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        counts = Counter(nums)
        max_value = float("-inf")
        for key in counts:
            if key > max_value and counts[key] == 1:
                max_value = key
        return -1 if max_value == float("-inf") else max_value
