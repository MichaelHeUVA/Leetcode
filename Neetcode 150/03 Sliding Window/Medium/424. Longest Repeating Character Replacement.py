# https://leetcode.com/problems/longest-repeating-character-replacement/description/
from collections import defaultdict


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        frequency_map = defaultdict(int)
        longest = 0
        left = 0
        max_frequency = 0
        for right in range(len(s)):
            frequency_map[s[right]] += 1
            window_size = right - left + 1
            max_frequency = max(max_frequency, frequency_map[s[right]])

            while window_size > k + max_frequency:
                window_size -= 1
                frequency_map[s[left]] -= 1
                left += 1
            longest = max(longest, window_size)

        return longest
