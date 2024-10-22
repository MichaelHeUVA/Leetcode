# https://leetcode.com/problems/reshape-the-matrix/description/
from typing import List


class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        rows = len(mat)
        cols = len(mat[0])
        if rows * cols != r * c:
            return mat
        temp = []
        for row in range(rows):
            for col in range(cols):
                temp.append(mat[row][col])
        count = 0
        output = []
        for row in range(r):
            p = []
            for col in range(c):
                p.append(temp[count])
                count += 1
            output.append(p)
        return output
