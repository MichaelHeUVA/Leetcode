# https://leetcode.com/problems/regular-expression-matching/description/


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = {}

        def dfs(i, j):
            if (i, j) in dp:
                return dp[(i, j)]
            if i == len(s) and j == len(p):
                return True
            if j == len(p):
                return False

            match = i < len(s) and (s[i] == p[j] or p[j] == ".")
            dp[(i, j)] = 0
            if j + 1 < len(p) and p[j + 1] == "*":
                dp[(i, j)] = dfs(i, j + 2) or (match and dfs(i + 1, j))
            elif match:
                dp[(i, j)] = dfs(i + 1, j + 1)
            else:
                dp[(i, j)] = False

            return dp[(i, j)]

        return dfs(0, 0)
