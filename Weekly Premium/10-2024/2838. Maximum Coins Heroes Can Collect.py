# https://leetcode.com/problems/maximum-coins-heroes-can-collect/description/
from collections import defaultdict
from typing import List


class Solution:
    def maximumCoins(
        self, heroes: List[int], monsters: List[int], coins: List[int]
    ) -> List[int]:
        monster_coins = defaultdict(int)
        for i, monster in enumerate(monsters):
            monster_coins[monster] += coins[i]

        sorted_monsters = sorted(monster_coins.keys())
        for i in range(1, len(sorted_monsters)):
            monster_coins[sorted_monsters[i]] += monster_coins[sorted_monsters[i - 1]]

        output = []
        for hero in heroes:
            left = 0
            right = len(sorted_monsters) - 1
            k = 0
            while left <= right:
                mid = (left + right) // 2
                if sorted_monsters[mid] <= hero:
                    k = sorted_monsters[mid]
                    left = mid + 1
                else:
                    right = mid - 1

            output.append(monster_coins[k])
        return output
