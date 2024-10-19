# https://leetcode.com/problems/distinct-subsequences/description/


class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        if len(t) > len(s):
            return 0
        dp = {}

        def dfs(si, ti):
            if (si, ti) in dp:
                return dp[(si, ti)]
            if ti == len(t):
                return 1
            if si == len(s):
                return 0
            if s[si] == t[ti]:
                dp[(si, ti)] = dfs(si + 1, ti + 1) + dfs(si + 1, ti)
            else:
                dp[(si, ti)] = dfs(si + 1, ti)
            return dp[(si, ti)]

        return dfs(0, 0)
