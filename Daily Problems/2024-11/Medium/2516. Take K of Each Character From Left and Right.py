# https://leetcode.com/problems/take-k-of-each-character-from-left-and-right/description/?envType=daily-question&envId=2024-11-20
from collections import Counter


class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        n = len(s)
        counts = Counter(s)
        for key in ["a", "b", "c"]:
            if counts[key] < k:
                return -1
        left = 0
        right = n - 1
        window = Counter()
        left = 0
        max_window = 0
        for right in range(n):
            window[s[right]] += 1
            while left <= right and (
                counts["a"] - window["a"] < k
                or counts["b"] - window["b"] < k
                or counts["c"] - window["c"] < k
            ):
                window[s[left]] -= 1
                left += 1
            max_window = max(max_window, right - left + 1)

        return n - max_window
