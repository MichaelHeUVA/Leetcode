# https://leetcode.com/problems/open-the-lock/description/
from collections import deque
from typing import List


class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadends_set = set(deadends)

        if "0000" in deadends_set:
            return -1

        q = deque([(0, "0000")])
        visited = set("0000")

        while q:
            size = len(q)
            for _ in range(size):
                distance, comb = q.popleft()
                if comb == target:
                    return distance
                for i in range(4):
                    current_digit = int(comb[i])
                    for move in [-1, 1]:
                        new_digit = (current_digit + move) % 10
                        new_state = comb[:i] + str(new_digit) + comb[i + 1 :]
                        if new_state not in visited and new_state not in deadends_set:
                            q.append((distance + 1, new_state))
                            visited.add(new_state)

        return -1
