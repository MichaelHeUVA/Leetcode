# https://leetcode.com/problems/eliminate-maximum-number-of-monsters/description/
from typing import List


class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        for i in range(len(dist)):
            dist[i] /= speed[i]
        dist.sort()
        ans = 0
        for i in range(len(dist)):
            if dist[i] <= i:
                break
            ans += 1

        return ans
