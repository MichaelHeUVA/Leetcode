# https://leetcode.com/problems/subsets/description/
from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        def backtrack(path, index):
            result.append(path.copy())
            for i in range(index, len(nums)):
                path.append(nums[i])
                backtrack(path, i + 1)
                path.pop()

        backtrack([], 0)
        return result
