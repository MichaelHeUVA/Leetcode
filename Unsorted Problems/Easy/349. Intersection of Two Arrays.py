# https://leetcode.com/problems/intersection-of-two-arrays/description/
from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        s1 = set(nums1)
        s2 = set(nums2)
        output = set()
        for num in nums1:
            if num in s2:
                output.add(num)
        for num in nums2:
            if num in s1:
                output.add(num)
        return list(output)
