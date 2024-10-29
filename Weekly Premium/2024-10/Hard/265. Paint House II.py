# https://leetcode.com/problems/paint-house-ii/description/?envType=weekly-question&envId=2024-10-29
from typing import List


class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        houses = len(costs)
        colors = len(costs[0])

        for house in range(1, houses):
            min_color = None
            second_min_color = None
            for color in range(colors):
                cost = costs[house - 1][color]
                if min_color is None or cost < costs[house - 1][min_color]:
                    second_min_color = min_color
                    min_color = color
                elif (
                    second_min_color is None
                    or cost < costs[house - 1][second_min_color]
                ):
                    second_min_color = color
            for color in range(colors):
                if color == min_color:
                    costs[house][color] += costs[house - 1][second_min_color]
                else:
                    costs[house][color] += costs[house - 1][min_color]

        return min(costs[-1])
