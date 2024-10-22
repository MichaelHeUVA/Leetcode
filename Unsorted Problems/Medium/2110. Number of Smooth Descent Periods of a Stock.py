# https://leetcode.com/problems/number-of-smooth-descent-periods-of-a-stock/description/
from typing import List


class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        output = len(prices)
        n = 0
        for i in range(1, len(prices)):
            diff = prices[i - 1] - prices[i]
            if diff == 1:
                n += 1
            else:
                output += (n * (n + 1)) // 2
                n = 0
        output += (n * (n + 1)) // 2
        return output
