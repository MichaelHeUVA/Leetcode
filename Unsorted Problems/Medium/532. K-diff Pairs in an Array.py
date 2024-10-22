# https://leetcode.com/problems/k-diff-pairs-in-an-array/description/
from collections import defaultdict
from typing import List


class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        m = defaultdict(int)
        s = set()
        for num in nums:
            if k + num in m:
                s.add(frozenset([num, k + num]))
            if -k + num in m:
                s.add(frozenset([num, -k + num]))
            m[num] = 1

        return len(s)
