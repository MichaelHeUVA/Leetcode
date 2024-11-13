# https://leetcode.com/problems/robot-collisions/description/
from collections import defaultdict
from typing import List


class Solution:
    def survivedRobotsHealths(
        self, positions: List[int], healths: List[int], directions: str
    ) -> List[int]:
        n = len(positions)
        pos_to_health = defaultdict(int)
        pos_to_index = defaultdict(int)
        for i in range(n):
            if directions[i] == "L":
                positions[i] = -positions[i]
            pos_to_health[positions[i]] = healths[i]
            pos_to_index[positions[i]] = i

        positions.sort(key=lambda x: abs(x))
        stack = []
        for i in range(n):
            while stack and positions[i] < 0 < stack[-1]:
                top = stack.pop()
                if pos_to_health[top] == pos_to_health[positions[i]]:
                    break
                elif pos_to_health[top] > pos_to_health[positions[i]]:
                    stack.append(top)
                    pos_to_health[top] -= 1
                    break
                else:
                    pos_to_health[positions[i]] -= 1
            else:
                stack.append(positions[i])

        return list(
            map(
                lambda x: pos_to_health[x], sorted(stack, key=lambda x: pos_to_index[x])
            )
        )
