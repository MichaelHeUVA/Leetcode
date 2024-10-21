# https://leetcode.com/problems/merge-triplets-to-form-target-triplet/description/
from typing import List


class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        first = False
        second = False
        third = False
        for triple in triplets:
            if (
                triple[0] <= target[0]
                and triple[1] <= target[1]
                and triple[2] <= target[2]
            ):
                if triple[0] == target[0]:
                    first = True
                if triple[1] == target[1]:
                    second = True
                if triple[2] == target[2]:
                    third = True
        return first and second and third
