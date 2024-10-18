# https://leetcode.com/problems/count-number-of-maximum-bitwise-or-subsets/description/?envType=daily-question&envId=2024-10-18
from typing import List


class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        def find_or(path):
            total_or = 0
            for num in path:
                total_or |= num
            return total_or

        max_bitwise_or = find_or(nums)

        def backtrack(index, path):
            nonlocal output
            if find_or(path) == max_bitwise_or:
                output += 1

            for i in range(index, len(nums)):
                path.append(nums[i])
                backtrack(i + 1, path)
                path.pop()

        output = 0
        backtrack(0, [])
        return output
