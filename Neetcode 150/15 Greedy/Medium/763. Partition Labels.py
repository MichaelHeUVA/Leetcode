# https://leetcode.com/problems/partition-labels/description/
from collections import defaultdict
from typing import List


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = defaultdict(int)
        for i in range(len(s)):
            last[s[i]] = i
        result = []
        start = 0
        end = 0
        for i, c in enumerate(s):
            end = max(end, last[c])
            if i == end:
                result.append(end - start + 1)
                start = i + 1
        return result
