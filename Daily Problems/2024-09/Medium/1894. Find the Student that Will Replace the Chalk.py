# https://leetcode.com/problems/find-the-student-that-will-replace-the-chalk/description/?envType=daily-question&envId=2024-09-02
from typing import List


class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        s = sum(chalk)
        remainder = k % s
        for i in range(len(chalk)):
            if remainder < chalk[i]:
                return i
            remainder -= chalk[i]
