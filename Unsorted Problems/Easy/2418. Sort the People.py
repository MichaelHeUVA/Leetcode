# https://leetcode.com/problems/sort-the-people/description/
from collections import defaultdict
from typing import List


class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        m = defaultdict(str)
        for i in range(len(names)):
            m[heights[i]] = names[i]
        output = []
        for height in sorted(heights, reverse=True):
            output.append(m[height])
        return output
