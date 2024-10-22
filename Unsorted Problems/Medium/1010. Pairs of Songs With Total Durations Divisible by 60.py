# https://leetcode.com/problems/pairs-of-songs-with-total-durations-divisible-by-60/description/
from collections import defaultdict
from typing import List


class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        complement_map = defaultdict(int)
        pairs = 0
        for length in time:
            mod_length = length % 60
            if mod_length == 0 and complement_map[0] > 0:
                pairs += complement_map[0]
            elif complement_map[60 - mod_length] > 0:
                pairs += complement_map[60 - mod_length]
            complement_map[mod_length] += 1

        return pairs
