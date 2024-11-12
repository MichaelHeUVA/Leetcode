# https://leetcode.com/problems/most-beautiful-item-for-each-query/description/?envType=daily-question&envId=2024-11-12
from typing import List


class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        items.sort()
        max_beauty = items[0][1]
        for i in range(len(items)):
            max_beauty = max(max_beauty, items[i][1])
            items[i][1] = max_beauty
        output = []
        for q in queries:
            left = 0
            right = len(items) - 1
            max_beauty = 0
            while left <= right:
                mid = (left + right) // 2
                if items[mid][0] <= q:
                    left = mid + 1
                    max_beauty = max(max_beauty, items[mid][1])
                else:
                    right = mid - 1
            output.append(max_beauty)
        return output
