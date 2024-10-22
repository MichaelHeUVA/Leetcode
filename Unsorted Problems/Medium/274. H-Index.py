# https://leetcode.com/problems/h-index/description/
from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        left = 0
        right = len(citations)
        k = 0
        while left <= right:
            mid = (left + right) // 2
            count = 0
            for num in citations:
                if mid <= num:
                    count += 1
            if count == mid:
                return mid
            elif count >= mid:
                k = mid
                left = mid + 1
            elif count < mid:
                right = mid - 1

        return k
