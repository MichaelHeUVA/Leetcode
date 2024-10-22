# https://leetcode.com/problems/find-the-maximum-number-of-elements-in-subset/description/
from collections import Counter
from typing import List


class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        counts = Counter(nums)
        max_elements = 1
        for key, val in counts.items():
            count = 0
            if key == 1:
                if val % 2 == 0:
                    count = val - 1
                else:
                    count = val
            elif key != 1 and val >= 2:
                while key**2 in counts:
                    if counts[key**2] == 1 or key**4 not in counts:
                        count += 3
                        break
                    elif counts[key**2] >= 2:
                        count += 2
                        key = key**2

            max_elements = max(max_elements, count)
        return max_elements
