# https://leetcode.com/problems/make-the-string-great/?envType=daily-question&envId=2024-04-05


class Solution:
    def makeGood(self, s: str) -> str:
        i = 0
        while i < len(s) - 1:
            if (ord(s[i]) - ord("A") == ord(s[i + 1]) - ord("a")) or (
                ord(s[i]) - ord("a") == ord(s[i + 1]) - ord("A")
            ):
                s = s[:i] + s[i + 2 :]  # Skip the matching pair of characters
                i = max(
                    0, i - 1
                )  # Step back to check for new adjacent pairs that might form after
            else:
                i += 1
        return s
