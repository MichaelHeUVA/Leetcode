# https://leetcode.com/problems/flood-fill/description/
from typing import List


class Solution:
    def floodFill(
        self, image: List[List[int]], sr: int, sc: int, color: int
    ) -> List[List[int]]:
        if image[sr][sc] == color:
            return image
        orignal_num = image[sr][sc]

        def dfs(row, col):
            if (
                row < 0
                or row >= len(image)
                or col < 0
                or col >= len(image[0])
                or image[row][col] != orignal_num
            ):
                return
            image[row][col] = color
            dfs(row + 1, col)
            dfs(row - 1, col)
            dfs(row, col + 1)
            dfs(row, col - 1)

        dfs(sr, sc)
        return image
