# https://leetcode.com/problems/image-overlap/description/
from collections import defaultdict
from typing import List


class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        rows = len(img1)
        cols = len(img1[0])
        img1_set = set()
        img2_set = set()
        for row in range(rows):
            for col in range(cols):
                if img1[row][col] == 1:
                    img1_set.add((row, col))
                if img2[row][col] == 1:
                    img2_set.add((row, col))

        translations = defaultdict(int)
        for row1, col1 in img1_set:
            for row2, col2 in img2_set:
                translations[(row2 - row1, col2 - col1)] += 1
        return max(translations.values(), default=0)
