# https://leetcode.com/problems/walking-robot-simulation/description/?envType=daily-question&envId=2024-09-04
from typing import List


class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        obst = set()
        for x, y in obstacles:
            obst.add((x, y))
        x, y = 0, 0
        furthest = 0
        direction = 0  # n = +y, e = +x, s = -y, w = -x
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for command in commands:
            if command == -1:
                direction = (direction + 1) % 4
            elif command == -2:
                direction = (direction - 1) % 4
            else:
                dx, dy = directions[direction]
                for i in range(command):
                    if (x + dx, y + dy) in obst:
                        break
                    x, y = x + dx, y + dy
            furthest = max(furthest, x**2 + y**2)
        return furthest
