# https://leetcode.com/problems/top-k-frequent-elements/description/
from collections import Counter
import heapq
from typing import List


# Heap / Priority Queue Solution
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        pq = []
        for key in counts:
            heapq.heappush(pq, (-counts[key], key))
        output = []
        i = 0
        while i < k:
            output.append(heapq.heappop(pq)[1])
            i += 1

        return output


# Bucket Sort
class Solution:  # noqa: F811
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)

        buckets = [[] for _ in range(len(nums) + 1)]

        for key, value in counts.items():
            buckets[value].append(key)

        output = []

        for i in range(len(buckets) - 1, 0, -1):
            output += buckets[i]
            if len(output) == k:
                return output
