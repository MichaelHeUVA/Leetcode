# https://leetcode.com/problems/brick-wall/description/
from collections import Counter
from typing import List


class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        count = Counter()
        for row in wall:
            total = 0
            for col in range(len(row) - 1):
                total += row[col]
                count[total] += 1

        return len(wall) - max(count.values(), default=0)
