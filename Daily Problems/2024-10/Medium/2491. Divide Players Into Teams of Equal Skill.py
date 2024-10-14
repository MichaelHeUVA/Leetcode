# https://leetcode.com/problems/divide-players-into-teams-of-equal-skill/description/?envType=daily-question&envId=2024-10-04
from collections import Counter
from typing import List


class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        total_sum = sum(skill)

        if total_sum % (len(skill) // 2) != 0:
            return -1

        pair_sum = total_sum // (len(skill) // 2)
        counts = Counter(skill)
        chemistry = 0

        for num, count in counts.items():
            complement = pair_sum - num
            if complement not in counts or count != counts[complement]:
                return -1
            chemistry += num * complement * count

        return chemistry // 2
