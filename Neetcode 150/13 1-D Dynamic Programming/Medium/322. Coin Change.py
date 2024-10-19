# https://leetcode.com/problems/coin-change/description/
from typing import List


# Top-down DP
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = {}  # {remainder: number of coins}

        def dfs(remainder):
            if remainder == 0:
                return 0
            if remainder not in dp:
                dp[remainder] = float("inf")
                for coin in coins:
                    if coin <= remainder:
                        dp[remainder] = min(dp[remainder], dfs(remainder - coin) + 1)
            return dp[remainder]

        min_count = dfs(amount)
        return -1 if min_count == float("inf") else min_count


# Bottom-up DP
class Solution:  # noqa F811
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float("inf")] * (amount + 1)
        dp[0] = 0
        for i in range(1, amount + 1):
            for coin in coins:
                if i - coin >= 0:
                    dp[i] = min(dp[i], dp[i - coin] + 1)

        return dp[amount] if dp[amount] != float("inf") + 1 else -1
