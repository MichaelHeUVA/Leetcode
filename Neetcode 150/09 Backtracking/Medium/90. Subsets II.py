# https://leetcode.com/problems/subsets-ii/description/
from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []

        def backtrack(path, index):
            result.append(path.copy())
            for i in range(index, len(nums)):
                if i != index and nums[i] == nums[i - 1]:
                    continue
                path.append(nums[i])
                backtrack(path, i + 1)
                path.pop()

        backtrack([], 0)
        return result
