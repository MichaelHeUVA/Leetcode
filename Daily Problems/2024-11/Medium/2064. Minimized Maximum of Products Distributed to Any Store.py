# https://leetcode.com/problems/minimized-maximum-of-products-distributed-to-any-store/description/
from math import ceil
from typing import List


class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        def can_distribute(mid):
            total = 0
            for q in quantities:
                total += ceil(q / mid)
            return total <= n

        left = 1
        right = max(quantities)
        while left <= right:
            mid = (left + right) // 2
            if can_distribute(mid):
                right = mid - 1
            else:
                left = mid + 1
        return left
