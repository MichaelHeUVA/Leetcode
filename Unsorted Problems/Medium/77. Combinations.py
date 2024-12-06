# https://leetcode.com/problems/combinations/description/
from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        output = []

        def backtrack(num, combination):
            if len(combination) == k:
                output.append(combination[::])

            for i in range(num, n + 1):
                combination.append(i)
                backtrack(i + 1, combination)
                combination.pop()

        backtrack(1, [])
        return output
