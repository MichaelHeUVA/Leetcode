# https://leetcode.com/problems/zigzag-conversion/description/


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        matrix = [[] for _ in range(numRows)]
        row = 0
        down = True
        for char in s:
            matrix[row].append(char)
            if down:
                row += 1
            else:
                row -= 1
            if row == 0 or row == numRows - 1:
                down = not down
        output = []
        for row in matrix:
            output.extend(row)

        return "".join(output)
