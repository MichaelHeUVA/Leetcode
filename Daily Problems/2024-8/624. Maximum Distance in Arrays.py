# https://leetcode.com/problems/maximum-distance-in-arrays/description/?envType=daily-question&envId=2024-08-16
from typing import List


class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        min_int = arrays[0][0]
        max_int = arrays[0][-1]
        max_distance = float("-inf")
        for i in range(1, len(arrays)):
            max_distance = max(
                max_distance, abs(min_int - arrays[i][-1]), abs(max_int - arrays[i][0])
            )
            min_int = min(min_int, arrays[i][0])
            max_int = max(max_int, arrays[i][-1])
        return max_distance
