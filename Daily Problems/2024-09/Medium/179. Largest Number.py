# https://leetcode.com/problems/largest-number/?envType=daily-question&envId=2024-09-18
from functools import cmp_to_key
from typing import List


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        string_nums = list(map(str, nums))

        def comparator(a, b):
            if a + b > b + a:
                return -1
            else:
                return 1

        string_nums.sort(key=cmp_to_key(comparator))
        if string_nums[0] == "0":
            return "0"
        return "".join(string_nums)
