# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/description/
from typing import List


class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        dp = {}

        def dfs(day, can_buy):
            if (day, can_buy) in dp:
                return dp[(day, can_buy)]
            if day == len(prices):
                return 0
            if can_buy:
                buy = dfs(day + 1, not can_buy) - prices[day]
                dont_buy = dfs(day + 1, can_buy)
                dp[(day, can_buy)] = max(buy, dont_buy)
            else:
                sell = dfs(day + 1, not can_buy) + prices[day] - fee
                dont_sell = dfs(day + 1, can_buy)
                dp[(day, can_buy)] = max(sell, dont_sell)
            return dp[(day, can_buy)]

        return dfs(0, True)
