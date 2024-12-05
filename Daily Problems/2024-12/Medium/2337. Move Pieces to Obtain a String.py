# https://leetcode.com/problems/move-pieces-to-obtain-a-string/description/?envType=daily-question&envId=2024-12-05


class Solution:
    def canChange(self, start: str, target: str) -> bool:
        s_q = []
        t_q = []

        for i in range(len(start)):
            if start[i] != "_":
                s_q.append((start[i], i))
            if target[i] != "_":
                t_q.append((target[i], i))

        if len(s_q) != len(t_q):
            return False

        while len(s_q) != 0:
            s_c, s_i = s_q.pop()
            t_c, t_i = t_q.pop()
            if s_c != t_c or (s_c == "L" and s_i < t_i) or (s_c == "R" and s_i > t_i):
                return False

        return True
