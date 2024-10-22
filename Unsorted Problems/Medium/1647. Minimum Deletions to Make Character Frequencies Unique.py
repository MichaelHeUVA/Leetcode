# https://leetcode.com/problems/minimum-deletions-to-make-character-frequencies-unique/description/


class Solution:
    def minDeletions(self, s: str) -> int:
        frequency = [0] * 26
        for char in s:
            frequency[ord(char) - ord("a")] += 1
        frequency.sort(reverse=True)

        output = 0
        max_allowed_frequency = len(s)

        for freq in frequency:
            if freq > max_allowed_frequency:
                output += freq - max_allowed_frequency
                freq = max_allowed_frequency
            max_allowed_frequency = max(0, freq - 1)
        return output
