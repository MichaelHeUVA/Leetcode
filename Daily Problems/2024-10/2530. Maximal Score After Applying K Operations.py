# https://leetcode.com/problems/maximal-score-after-applying-k-operations/description/?envType=daily-question&envId=2024-10-14
from heapq import heappush, heappop
from typing import List
from math import ceil


class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        max_heap = []
        for num in nums:
            heappush(max_heap, -num)

        output = 0
        for _ in range(k):
            num = -heappop(max_heap)
            output += num
            heappush(max_heap, -ceil(num / 3))
        return output
