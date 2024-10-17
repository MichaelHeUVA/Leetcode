# https://leetcode.com/problems/combination-sum-ii/description/
from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []

        def backtrack(index, comb, comb_sum):
            if comb_sum == target:
                result.append(comb.copy())
                return
            if comb_sum > target:
                return

            for i in range(index, len(candidates)):
                if i > index and candidates[i] == candidates[i - 1]:
                    continue
                comb.append(candidates[i])
                backtrack(i + 1, comb, comb_sum + candidates[i])
                comb.pop()

        backtrack(0, [], 0)
        return result
