# https://leetcode.com/problems/minimum-total-distance-traveled/description/?envType=daily-question&envId=2024-10-31
from typing import List


class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        robot.sort()
        factory.sort()
        factory_positions = []
        for fact in factory:
            for _ in range(fact[1]):
                factory_positions.append(fact[0])

        dp = [
            [float("inf")] * (len(factory_positions) + 1) for _ in range(len(robot) + 1)
        ]
        for row in range(len(factory_positions) + 1):
            dp[0][row] = 0

        for row in range(1, len(robot) + 1):
            for col in range(1, len(factory_positions) + 1):
                dp[row][col] = min(
                    dp[row][col - 1],
                    dp[row - 1][col - 1]
                    + abs(robot[row - 1] - factory_positions[col - 1]),
                )

        return dp[-1][-1]
