# https://leetcode.com/problems/hand-of-straights/description/
from collections import Counter
from heapq import heapify, heappop
from typing import List


class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        count = Counter(hand)
        heap = list(count.keys())
        heapify(heap)
        while heap:
            start = heap[0]
            for i in range(start, start + groupSize):
                if i not in count:
                    return False
                count[i] -= 1
                if count[i] == 0:
                    if i != heap[0]:
                        return False
                    heappop(heap)
        return True
