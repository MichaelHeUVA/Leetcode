# https://leetcode.com/problems/permutations/description/
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        used = [False] * len(nums)

        def backtrack(index, permutation):
            if len(permutation) == len(nums):
                res.append(permutation[:])
                return

            for i in range(len(nums)):
                if not used[i]:
                    permutation.append(nums[i])
                    used[i] = True
                    backtrack(i, permutation)
                    permutation.pop()
                    used[i] = False

        backtrack(0, [])
        return res
