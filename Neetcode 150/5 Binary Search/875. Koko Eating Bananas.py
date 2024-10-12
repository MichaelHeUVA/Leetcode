# https://leetcode.com/problems/koko-eating-bananas/description/
from typing import List
import math


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        k = 0
        while left <= right:
            mid = (left + right) // 2
            hours = 0
            for i in range(len(piles)):
                hours += math.ceil(piles[i] / mid)
            if hours <= h:
                k = mid
                right = mid - 1
            elif hours > h:
                left = mid + 1
        return k
