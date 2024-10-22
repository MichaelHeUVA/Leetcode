# https://leetcode.com/problems/count-good-triplets/description/
from bisect import bisect_left, bisect_right, insort
from typing import List


class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        n = len(arr)
        ans = 0
        for j in range(n - 2, -1, -1):
            arr_b = []
            for k in range(j + 1, n):
                diff = arr[j] - arr[k]
                if abs(diff) <= b:
                    insort(arr_b, diff)
            for i in range(j):
                diff = arr[i] - arr[j]
                if abs(diff) <= a:
                    lower = bisect_left(arr_b, -c - diff)
                    upper = bisect_right(arr_b, c - diff)
                    ans += upper - lower
        return ans
