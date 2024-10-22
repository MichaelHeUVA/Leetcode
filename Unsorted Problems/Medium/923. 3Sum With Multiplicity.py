# https://leetcode.com/problems/3sum-with-multiplicity/description/
from collections import defaultdict
from typing import List


class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        mod = int(1e9 + 7)
        output = 0
        for a in range(len(arr)):
            m = defaultdict(int)
            for b in range(a + 1, len(arr)):
                if arr[b] in m:
                    output += m[arr[b]]
                complement = target - arr[a] - arr[b]
                m[complement] += 1

        return output % mod
