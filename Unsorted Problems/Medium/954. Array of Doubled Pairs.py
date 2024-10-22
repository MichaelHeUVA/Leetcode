# https://leetcode.com/problems/array-of-doubled-pairs/description/
from collections import Counter
from typing import List


class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        m = Counter(arr)
        for key in sorted(arr, key=abs):
            if m[key] == 0:
                continue
            if key * 2 in m:
                m[key] -= 1
                m[key * 2] -= 1
        for key in m:
            if m[key] != 0:
                return False
        return True
