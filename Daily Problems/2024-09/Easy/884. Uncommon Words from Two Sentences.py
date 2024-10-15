# https://leetcode.com/problems/uncommon-words-from-two-sentences/description/?envType=daily-question&envId=2024-09-17
from collections import Counter
from typing import List


class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        s1_counts = Counter(s1.split())
        s2_counts = Counter(s2.split())
        output = []
        for key in s1_counts:
            if key not in s2_counts and s1_counts[key] == 1:
                output.append(key)
        for key in s2_counts:
            if key not in s1_counts and s2_counts[key] == 1:
                output.append(key)
        return output
