# https://leetcode.com/problems/minimum-absolute-difference/description/
from typing import List


class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        min_ad = float("inf")
        output = []
        for i in range(len(arr) - 1):
            mae = arr[i + 1] - arr[i]
            if mae < min_ad:
                output = []
                min_ad = mae
                output.append([arr[i], arr[i + 1]])
            elif mae == min_ad:
                output.append([arr[i], arr[i + 1]])

        return output
