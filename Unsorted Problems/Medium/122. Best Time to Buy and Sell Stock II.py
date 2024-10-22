# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/description/
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 0
        low = prices[0]
        high = prices[0]
        max_profit = 0
        while i < len(prices) - 1:
            while i < len(prices) - 1 and prices[i] >= prices[i + 1]:
                i += 1
            low = prices[i]
            while i < len(prices) - 1 and prices[i] <= prices[i + 1]:
                i += 1
            high = prices[i]
            max_profit += high - low
        return max_profit
