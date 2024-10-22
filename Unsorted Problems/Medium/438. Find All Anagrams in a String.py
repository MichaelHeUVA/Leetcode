# https://leetcode.com/problems/find-all-anagrams-in-a-string/description/
from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []
        p_map = [0] * 26
        s_map = [0] * 26
        for i in range(len(p)):
            s_map[ord(s[i]) - ord("a")] += 1
            p_map[ord(p[i]) - ord("a")] += 1
        output = []
        left = 0
        for right in range(len(p), len(s)):
            if s_map == p_map:
                output.append(left)
            s_map[ord(s[left]) - ord("a")] -= 1
            s_map[ord(s[right]) - ord("a")] += 1
            left += 1
        if s_map == p_map:
            output.append(left)
        return output
