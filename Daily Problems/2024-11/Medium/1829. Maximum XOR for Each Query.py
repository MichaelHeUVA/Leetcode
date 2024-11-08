# https://leetcode.com/problems/maximum-xor-for-each-query/description/?envType=daily-question&envId=2024-11-08
from typing import List


class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        n = len(nums)
        prefix_xor = [0] * (n + 1)
        for i, num in enumerate(nums):
            prefix_xor[i + 1] = prefix_xor[i] ^ num
        max_num = 2**maximumBit - 1
        output = []
        for i in range(n, 0, -1):
            output.append(max_num ^ prefix_xor[i])
        return output
