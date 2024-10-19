# https://leetcode.com/problems/maximum-product-subarray/description/
from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        current_max = 1
        current_min = 1
        max_product = nums[0]
        for num in nums:
            temp = (num * current_max, num * current_min, num)
            current_max = max(temp)
            current_min = min(temp)
            max_product = max(max_product, current_max)

        return max_product
