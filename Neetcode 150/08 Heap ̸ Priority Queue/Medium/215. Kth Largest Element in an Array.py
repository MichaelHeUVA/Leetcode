# https://leetcode.com/problems/kth-largest-element-in-an-array/description/
from heapq import heappush, heappushpop
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minheap = []
        for num in nums:
            if len(minheap) < k:
                heappush(minheap, num)
            else:
                if num > minheap[0]:
                    heappushpop(minheap, num)
        return minheap[0]
