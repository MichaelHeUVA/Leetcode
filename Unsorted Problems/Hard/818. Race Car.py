# https://leetcode.com/problems/race-car/description/
from collections import deque


class Solution:
    def racecar(self, target: int) -> int:
        q = deque([(0, 1, 0)])  # (pos, speed, steps)
        while q:
            pos, speed, steps = q.popleft()

            if pos == target:
                return steps

            q.append((pos + speed, speed * 2, steps + 1))
            if (pos + speed > target and speed > 0) or (
                pos + speed < target and speed < 0
            ):
                if speed > 0:
                    q.append((pos, -1, steps + 1))
                else:
                    q.append((pos, 1, steps + 1))
