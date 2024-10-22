# https://leetcode.com/problems/divide-array-in-sets-of-k-consecutive-numbers/description/
from collections import Counter
from heapq import heapify, heappop
from typing import List


class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        count = Counter(nums)
        heap = list(count.keys())
        heapify(heap)
        while heap:
            start = heap[0]
            for i in range(start, start + k):
                if i not in count:
                    return False
                count[i] -= 1
                if count[i] == 0:
                    if i != heap[0]:
                        return False
                    heappop(heap)
        return True
