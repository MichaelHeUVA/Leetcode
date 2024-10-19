# https://leetcode.com/problems/longest-common-subsequence/description/


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if text1 == text2:
            return len(text1)
        rows = len(text1)
        cols = len(text2)
        dp = [[0] * (cols + 1) for _ in range(rows + 1)]

        for row in reversed(range(rows)):
            for col in reversed(range(cols)):
                if text1[row] == text2[col]:
                    dp[row][col] = 1 + dp[row + 1][col + 1]
                else:
                    dp[row][col] = max(dp[row + 1][col], dp[row][col + 1])
        return dp[0][0]
