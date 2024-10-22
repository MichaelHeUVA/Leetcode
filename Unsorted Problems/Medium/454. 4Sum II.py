# https://leetcode.com/problems/4sum-ii/description/
from collections import defaultdict
from typing import List


class Solution:
    def fourSumCount(
        self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]
    ) -> int:
        one_plus_two = []
        three_plus_four = defaultdict(int)
        for num1 in nums1:
            for num2 in nums2:
                one_plus_two.append(num1 + num2)
        for num3 in nums3:
            for num4 in nums4:
                three_plus_four[num3 + num4] += 1
        output = 0
        for num in one_plus_two:
            if -num in three_plus_four:
                output += three_plus_four[-num]
        return output
