# https://leetcode.com/problems/xor-queries-of-a-subarray/description/?envType=daily-question&envId=2024-09-13
from typing import List


class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        prefix_sum = [0] * (len(arr) + 1)
        for i in range(len(arr)):
            prefix_sum[i + 1] = prefix_sum[i] ^ arr[i]

        output = []
        for x, y in queries:
            output.append(prefix_sum[y + 1] ^ prefix_sum[x])

        return output
