# https://leetcode.com/problems/permutations-ii/description/
from collections import Counter
from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        output = []
        counts = Counter(nums)
        permutation = []

        def backtrack():
            if len(permutation) == len(nums):
                output.append(permutation[::])
                return

            for n in counts:
                if counts[n] > 0:
                    permutation.append(n)
                    counts[n] -= 1

                    backtrack()

                    counts[n] += 1
                    permutation.pop()

        backtrack()
        return list(output)
