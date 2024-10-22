# https://leetcode.com/problems/kth-largest-element-in-a-stream/description/
from heapq import heappush, heappop, heapify
from typing import List


class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        heapify(nums)
        self.minheap = nums
        self.k = k

    def add(self, val: int) -> int:
        heappush(self.minheap, val)
        for _ in range(len(self.minheap) - self.k):
            heappop(self.minheap)
        return self.minheap[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
