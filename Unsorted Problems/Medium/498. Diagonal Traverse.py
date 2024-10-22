# https://leetcode.com/problems/diagonal-traverse/description/
from collections import defaultdict
from typing import List


class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        output = []
        rows = len(mat)
        cols = len(mat[0])
        m = defaultdict(list)
        for row in range(rows):
            for col in range(cols):
                m[row + col].append(mat[row][col])
        for i in range(rows + cols):
            if i % 2 == 0:
                output.extend(reversed(m[i]))
            else:
                output.extend(m[i])
        return output
