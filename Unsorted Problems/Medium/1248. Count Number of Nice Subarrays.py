# https://leetcode.com/problems/count-number-of-nice-subarrays/description/
from typing import List


class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        odd = 0
        left = 0
        middle = 0
        output = 0

        for right in range(len(nums)):
            if nums[right] % 2 == 1:
                odd += 1
            while odd > k:
                if nums[left] % 2 == 1:
                    odd -= 1
                left += 1
                middle = left
            if odd == k:
                while nums[middle] % 2 != 1:
                    middle += 1
                output += middle - left + 1

        return output
