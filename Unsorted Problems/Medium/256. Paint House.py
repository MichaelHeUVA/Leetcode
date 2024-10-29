# https://leetcode.com/problems/paint-house/description/
from typing import List


class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        houses = len(costs)
        colors = len(costs[0])
        dp = [[float("inf")] * colors for _ in range(houses)]
        for color in range(colors):
            dp[0][color] = costs[0][color]
        for house in range(1, houses):
            for color in range(colors):
                for possible_color in range(colors):
                    if color != possible_color:
                        dp[house][color] = min(
                            dp[house][color],
                            dp[house - 1][possible_color] + costs[house][color],
                        )
        return min(dp[-1])
