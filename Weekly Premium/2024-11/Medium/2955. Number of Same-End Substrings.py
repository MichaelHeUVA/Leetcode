# https://leetcode.com/problems/number-of-same-end-substrings/description/?envType=weekly-question&envId=2024-11-01
from typing import List


class Solution:
    def sameEndSubstringCount(self, s: str, queries: List[List[int]]) -> List[int]:
        n = len(s)
        prefix_sum = [[0] * n for _ in range(26)]
        for i, char in enumerate(s):
            prefix_sum[ord(char) - ord("a")][i] += 1
        for frequency in prefix_sum:
            for i in range(1, n):
                frequency[i] += frequency[i - 1]

        output = []
        for start, end in queries:
            count = 0
            for frequency in prefix_sum:
                if start == 0:
                    left_count = 0
                else:
                    left_count = frequency[start - 1]
                right_count = frequency[end]
                frequency_in_range = right_count - left_count
                count += (frequency_in_range * (frequency_in_range + 1)) // 2
            output.append(count)

        return output
