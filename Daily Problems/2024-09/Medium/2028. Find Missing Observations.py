# https://leetcode.com/problems/find-missing-observations/description/?envType=daily-question&envId=2024-09-05
from typing import List


class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        total = len(rolls) + n
        missing = mean * total - sum(rolls)
        if missing < 1 * n or missing > 6 * n:
            return []
        base = missing // n
        output = [base] * n
        remainder = missing % n
        for i in range(remainder):
            output[i] += 1
        return output
