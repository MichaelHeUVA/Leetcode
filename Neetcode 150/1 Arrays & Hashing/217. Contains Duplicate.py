# https://leetcode.com/problems/contains-duplicate/description/
from collections import Counter
from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        counts = Counter(nums)
        for key in counts:
            if counts[key] > 1:
                return True
        return False
