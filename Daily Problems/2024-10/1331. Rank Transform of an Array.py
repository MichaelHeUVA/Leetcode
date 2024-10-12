# https://leetcode.com/problems/rank-transform-of-an-array/description/?envType=daily-question&envId=2024-10-02
from collections import defaultdict
from typing import List


class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        s = set(arr)
        sorted_array = sorted(list(s))
        m = defaultdict(int)
        for i in range(len(sorted_array)):
            m[sorted_array[i]] = i + 1
        output = []
        for num in arr:
            output.append(m[num])
        return output
