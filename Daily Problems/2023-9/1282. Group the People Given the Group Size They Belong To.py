# https://leetcode.com/problems/group-the-people-given-the-group-size-they-belong-to/description/?envType=daily-question&envId=2023-09-11
from collections import defaultdict
from typing import List


class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        n = len(groupSizes)
        output = []
        groups = defaultdict(list)
        for i in range(n):
            groups[groupSizes[i]].append(i)
            if len(groups[groupSizes[i]]) == groupSizes[i]:
                output.append(groups[groupSizes[i]])
                del groups[groupSizes[i]]

        return output
