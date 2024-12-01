# https://leetcode.com/problems/check-if-n-and-its-double-exist/description/?envType=daily-question&envId=2024-12-01
from collections import Counter
from typing import List


class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        counts = Counter(arr)
        for num in arr:
            if num == 0 and counts[num] > 1:
                return True
            elif num != 0 and num * 2 in counts:
                return True
        return False
