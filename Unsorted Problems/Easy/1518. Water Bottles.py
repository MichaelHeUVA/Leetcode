# https://leetcode.com/problems/water-bottles/description/


class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        total_bottles = 0
        while numBottles >= numExchange:
            k = numBottles // numExchange

            total_bottles += numExchange * k
            numBottles -= numExchange * k

            numBottles += k

        return total_bottles + numBottles
