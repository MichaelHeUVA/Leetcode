# https://leetcode.com/problems/robot-return-to-origin/description/
from collections import Counter


class Solution:
    def judgeCircle(self, moves: str) -> bool:
        m = Counter(moves)
        return True if m["U"] == m["D"] and m["L"] == m["R"] else False
