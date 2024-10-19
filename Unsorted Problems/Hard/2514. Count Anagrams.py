# https://leetcode.com/problems/count-anagrams/description/
from collections import Counter
from math import factorial


class Solution:
    def countAnagrams(self, s: str) -> int:
        words = s.split(" ")
        ans = 1
        for word in words:
            numerator = factorial(len(word))
            w_map = Counter(word)
            denominator = 1
            for value in w_map.values():
                denominator *= factorial(value)
            ans *= numerator // denominator % (10**9 + 7)

        return ans % (10**9 + 7)
