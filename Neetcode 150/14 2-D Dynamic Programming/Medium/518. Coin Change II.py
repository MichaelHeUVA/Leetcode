# https://leetcode.com/problems/coin-change-ii/description/
from typing import List


# Top-down DP
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = {}  # {(index, remainder): number of ways}

        def dfs(i, remainder):
            if remainder == 0:
                return 1
            if remainder < 0:
                return 0
            if i == len(coins):
                return 0
            if (i, remainder) in dp:
                return dp[(i, remainder)]
            dp[(i, remainder)] = dfs(i + 1, remainder) + dfs(i, remainder - coins[i])
            return dp[(i, remainder)]

        return dfs(0, amount)


# Bottom-up DP
class Solution:  # noqa F811
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1

        for coin in coins:
            for j in range(coin, amount + 1):
                dp[j] += dp[j - coin]

        return dp[amount]
