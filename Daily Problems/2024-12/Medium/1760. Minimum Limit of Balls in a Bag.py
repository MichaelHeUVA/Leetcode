# https://leetcode.com/problems/minimum-limit-of-balls-in-a-bag/description/?envType=daily-question&envId=2024-12-07
from math import ceil
from typing import List


class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        def is_possible(balls):
            total_operations = 0
            for num in nums:
                operations = ceil(num / balls) - 1
                total_operations += operations

                if total_operations > maxOperations:
                    return False
            return True

        left = 1
        right = max(nums)
        while left <= right:
            mid = (left + right) // 2
            if is_possible(mid):
                right = mid - 1
            else:
                left = mid + 1

        return left
