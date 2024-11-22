# https://leetcode.com/problems/flip-columns-for-maximum-number-of-equal-rows/description/?envType=daily-question&envId=2024-11-22
from collections import Counter
from typing import List


class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        pattern_count = Counter()
        for row in matrix:
            if row[0] == 0:
                for i in range(len(row)):
                    row[i] = 1 - row[i]
            pattern_count[tuple(row)] += 1

        return pattern_count.most_common(1)[0][1]
