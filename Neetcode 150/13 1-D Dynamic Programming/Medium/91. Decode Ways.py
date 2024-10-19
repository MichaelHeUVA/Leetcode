# https://leetcode.com/problems/decode-ways/description/


class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == "0":
            return 0

        dp = [0] * (len(s) + 1)
        dp[0] = 1
        dp[1] = 1

        for i in range(2, len(s) + 1):
            one_digit = int(s[i - 1])
            two_digit = int(s[i - 2 : i])

            if one_digit != 0:
                dp[i] += dp[i - 1]

            if 10 <= two_digit <= 26:
                dp[i] += dp[i - 2]

        return dp[len(s)]
