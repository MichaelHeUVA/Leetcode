# https://leetcode.com/problems/intersection-of-three-sorted-arrays/description/?envType=weekly-question&envId=2024-11-08
from typing import List


class Solution:
    def arraysIntersection(
        self, arr1: List[int], arr2: List[int], arr3: List[int]
    ) -> List[int]:
        set1 = set(arr1)
        set2 = set(arr2)
        output = []
        for num in arr3:
            if num in set1 and num in set2:
                output.append(num)

        return output
