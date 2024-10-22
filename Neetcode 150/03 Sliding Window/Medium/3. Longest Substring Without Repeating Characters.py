# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        frequency_map = set()
        output = 0

        for right in range(len(s)):
            while s[right] in frequency_map:
                frequency_map.remove(s[left])
                left += 1
            frequency_map.add(s[right])
            output = max(output, right - left + 1)

        return output
