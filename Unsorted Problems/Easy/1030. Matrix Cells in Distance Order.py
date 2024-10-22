# https://leetcode.com/problems/matrix-cells-in-distance-order/description/
from typing import List


class Solution:
    def allCellsDistOrder(
        self, rows: int, cols: int, rCenter: int, cCenter: int
    ) -> List[List[int]]:
        output = []
        for row in range(rows):
            for col in range(cols):
                output.append([row, col])

        output.sort(key=lambda x: abs(x[0] - rCenter) + abs(x[1] - cCenter))
        return output
