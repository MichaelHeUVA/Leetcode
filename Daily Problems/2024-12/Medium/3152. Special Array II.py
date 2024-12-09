# https://leetcode.com/problems/special-array-ii/description/?envType=daily-question&envId=2024-12-09
from typing import List


class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        n = len(nums)
        prefix = [0] * n
        prefix[0] = 0
        for i in range(1, n):
            if nums[i - 1] % 2 == nums[i] % 2:
                prefix[i] = prefix[i - 1] + 1
            else:
                prefix[i] = prefix[i - 1]
        print(prefix)
        output = []
        for left, right in queries:
            output.append(prefix[right] - prefix[left] == 0)
        return output
