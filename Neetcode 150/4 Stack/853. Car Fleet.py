# https://leetcode.com/problems/car-fleet/description/
from typing import List


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pos_and_spd = list(zip(position, speed))
        pos_and_spd.sort()
        stack = []
        for position, speed in pos_and_spd:
            time = (target - position) / speed
            while stack and stack[-1] <= time:
                stack.pop()
            stack.append(time)

        return len(stack)
