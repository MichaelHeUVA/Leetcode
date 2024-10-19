# https://leetcode.com/problems/interleaving-string/description/

# Top-down solution
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        dp = {}

        def dfs(s1i, s2i):
            if (s1i, s2i) in dp:
                return dp[(s1i, s2i)]
            if s1i == len(s1) and s2i == len(s2):
                return True
            s3i = s1i + s2i
            if s1i == len(s1):
                if s2[s2i:] != s3[s3i:]:
                    return False
                else:
                    return True
            if s2i == len(s2):
                if s1[s1i:] != s3[s3i:]:
                    return False
                else:
                    return True
            if s1[s1i] == s2[s2i] == s3[s3i]:
                dp[(s1i, s2i)] = dfs(s1i + 1, s2i) or dfs(s1i, s2i + 1)
            elif s1[s1i] == s3[s3i]:
                dp[(s1i, s2i)] = dfs(s1i + 1, s2i)
            elif s2[s2i] == s3[s3i]:
                dp[(s1i, s2i)] = dfs(s1i, s2i + 1)
            else:
                dp[(s1i, s2i)] = False
            return dp[(s1i, s2i)]

        return dfs(0, 0)


# Bottom-up solution
class Solution:  # noqa F811
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s3) != len(s1) + len(s2):
            return False
        dp = [False] * (len(s2) + 1)
        for i in range(len(s1) + 1):
            for j in range(len(s2) + 1):
                if i == 0 and j == 0:
                    dp[j] = True
                elif i == 0:
                    dp[j] = dp[j - 1] and s2[j - 1] == s3[i + j - 1]
                elif j == 0:
                    dp[j] = dp[j] and s1[i - 1] == s3[i + j - 1]
                else:
                    dp[j] = (dp[j] and s1[i - 1] == s3[i + j - 1]) or (
                        dp[j - 1] and s2[j - 1] == s3[i + j - 1]
                    )
        return dp[len(s2)]
