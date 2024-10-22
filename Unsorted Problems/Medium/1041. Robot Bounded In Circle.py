# https://leetcode.com/problems/robot-bounded-in-circle/description/


class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        x = 0
        y = 0
        facing = 0

        for i in instructions:
            if i == "L":
                facing = (facing - 1) % 4
            elif i == "R":
                facing = (facing + 1) % 4
            else:
                x += directions[facing][0]
                y += directions[facing][1]

        return (x == 0 and y == 0) or facing != 0
