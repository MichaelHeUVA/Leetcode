# https://leetcode.com/problems/number-of-unique-flavors-after-sharing-k-candies/description/?envType=weekly-question&envId=2024-11-15
from collections import Counter
from typing import List


class Solution:
    def shareCandies(self, candies: List[int], k: int) -> int:
        counts = Counter(candies)
        unique_candies = len(counts)
        lost_candies = 0
        for i in range(k):
            counts[candies[i]] -= 1
            if counts[candies[i]] == 0:
                lost_candies += 1
        output = unique_candies - lost_candies
        left = 0
        for right in range(k, len(candies)):
            counts[candies[left]] += 1
            if counts[candies[left]] == 1:
                lost_candies -= 1
            left += 1
            counts[candies[right]] -= 1
            if counts[candies[right]] == 0:
                lost_candies += 1
            output = max(output, unique_candies - lost_candies)
        return output
