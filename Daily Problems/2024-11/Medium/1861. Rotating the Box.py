# https://leetcode.com/problems/rotating-the-box/description/?envType=daily-question&envId=2024-11-23
from typing import List


class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        rows = len(box)
        cols = len(box[0])
        output = [[None] * rows for _ in range(cols)]
        for row in range(rows):
            for col in range(cols):
                output[col][row] = box[rows - 1 - row][col]

        for col in range(rows):
            lowest = cols - 1
            for row in range(cols - 1, -1, -1):
                if output[row][col] == "#":
                    output[row][col] = "."
                    output[lowest][col] = "#"
                    lowest -= 1
                if output[row][col] == "*":
                    lowest = row - 1
        return output
