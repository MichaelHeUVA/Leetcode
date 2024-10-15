# https://leetcode.com/problems/find-the-length-of-the-longest-common-prefix/description/?envType=daily-question&envId=2024-09-24
from typing import List


class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        arr1 = list(map(str, arr1))
        arr2 = list(map(str, arr2))

        arr1_prefix_set = set()
        for num in arr1:
            for i in range(1, len(num) + 1):
                arr1_prefix_set.add(num[0:i])

        longest_common_prefix = 0
        for num in arr2:
            for i in range(1, len(num) + 1):
                prefix = num[0:i]
                if prefix in arr1_prefix_set:
                    longest_common_prefix = max(longest_common_prefix, len(prefix))

        return longest_common_prefix
