# https://leetcode.com/problems/pascals-triangle/description/?envType=daily-question&envId=2023-09-08
from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        output = []
        for row_num in range(numRows):
            row = [0] * (row_num + 1)
            row[0] = 1
            row[-1] = 1
            for i in range(1, row_num):
                row[i] = output[row_num - 1][i - 1] + output[row_num - 1][i]
            output.append(row)
        return output
