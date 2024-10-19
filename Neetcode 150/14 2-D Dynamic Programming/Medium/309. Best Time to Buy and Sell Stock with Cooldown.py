# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/description/
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {}  # {(day, can buy): max profit}

        def dfs(day, can_buy):
            if day >= len(prices):
                return 0
            if (day, can_buy) in dp:
                return dp[(day, can_buy)]
            if can_buy:
                buy = dfs(day + 1, not can_buy) - prices[day]
                dont_buy = dfs(day + 1, can_buy)
                dp[(day, can_buy)] = max(buy, dont_buy)
            else:
                sell = dfs(day + 2, not can_buy) + prices[day]
                dont_sell = dfs(day + 1, can_buy)
                dp[(day, can_buy)] = max(sell, dont_sell)

            return dp[(day, can_buy)]

        return dfs(0, True)
