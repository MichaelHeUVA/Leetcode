# https://leetcode.com/problems/rotate-string/description/?envType=daily-question&envId=2024-11-03
from collections import deque


class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        s = deque(s)
        goal = deque(goal)
        for i in range(len(s)):
            if s == goal:
                return True
            s.append(s.popleft())

        return False
