# https://leetcode.com/problems/check-if-array-pairs-are-divisible-by-k/description/?envType=daily-question&envId=2024-10-01
from collections import defaultdict
from typing import List


class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        remainder = defaultdict(int)
        for num in arr:
            remainder[num % k] += 1

        for num in arr:
            if num % k == 0:
                if remainder[num % k] % 2 != 0:
                    return False

            elif remainder[num % k] != remainder[k - (num % k)]:
                return False
        return True
