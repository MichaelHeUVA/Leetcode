# https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/description/
from typing import List


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candies = max(candies)
        output = []
        for num in candies:
            if num + extraCandies >= max_candies:
                output.append(True)
            else:
                output.append(False)
        return output
