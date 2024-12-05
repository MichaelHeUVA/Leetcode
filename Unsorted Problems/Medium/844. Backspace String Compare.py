# https://leetcode.com/problems/backspace-string-compare/description/

# Stack solution
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s_list = []
        t_list = []
        for c in s:
            if c == "#":
                if s_list:
                    s_list.pop()
            else:
                s_list.append(c)
        for c in t:
            if c == "#":
                if t_list:
                    t_list.pop()
            else:
                t_list.append(c)
        return s_list == t_list


# Two pointer solution
class Solution:  # noqa F811
    def backspaceCompare(self, s: str, t: str) -> bool:
        s_pointer = len(s) - 1
        t_pointer = len(t) - 1
        s_skips = 0
        t_skips = 0
        while s_pointer >= 0 or t_pointer >= 0:
            while s_pointer >= 0:
                if s[s_pointer] == "#":
                    s_skips += 1
                    s_pointer -= 1
                elif s_skips > 0:
                    s_skips -= 1
                    s_pointer -= 1
                else:
                    break
            while t_pointer >= 0:
                if t[t_pointer] == "#":
                    t_skips += 1
                    t_pointer -= 1
                elif t_skips > 0:
                    t_skips -= 1
                    t_pointer -= 1
                else:
                    break
            if s_pointer >= 0 and t_pointer >= 0 and s[s_pointer] != t[t_pointer]:
                return False
            if (s_pointer >= 0) != (t_pointer >= 0):
                return False
            s_pointer -= 1
            t_pointer -= 1
        return True
