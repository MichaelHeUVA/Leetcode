# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        max_profit = 0
        for price in prices:
            if price < min_price:
                min_price = price
            max_profit = max(max_profit, price - min_price)
        return max_profit
