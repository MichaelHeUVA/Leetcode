# https://leetcode.com/problems/cutting-ribbons/description/?envType=weekly-question&envId=2024-12-08
from typing import List


class Solution:
    def maxLength(self, ribbons: List[int], k: int) -> int:
        def can_cut(mid):
            total_ribbons = 0
            for ribbon in ribbons:
                total_ribbons += ribbon // mid
                if total_ribbons >= k:
                    return False
            return True

        left = 1
        right = max(ribbons)
        while left <= right:
            mid = (left + right) // 2
            if can_cut(mid):
                right = mid - 1
            else:
                left = mid + 1

        return right
