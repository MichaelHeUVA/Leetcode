# https://leetcode.com/problems/lemonade-change/description/
from collections import defaultdict
from typing import List


class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        change = defaultdict(int)
        for bill in bills:
            if bill == 10:
                if change[5] >= 1:
                    change[5] -= 1
                else:
                    return False
            elif bill == 20:
                if change[5] >= 1 and change[10] >= 1:
                    change[10] -= 1
                    change[5] -= 1
                elif change[5] >= 3:
                    change[5] -= 3
                else:
                    return False
            change[bill] += 1
        return True
