# https://leetcode.com/problems/convert-1d-array-into-2d-array/description/?envType=daily-question&envId=2024-09-01
from typing import List


class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if len(original) != m * n:
            return []
        count = 0
        output = []
        for row in range(m):
            temp = []
            for col in range(n):
                temp.append(original[count])
                count += 1
            output.append(temp)
        return output
