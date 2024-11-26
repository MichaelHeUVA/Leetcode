# https://leetcode.com/problems/find-champion-ii/description/?envType=daily-question&envId=2024-11-26
from typing import List


class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        in_degrees = [0] * n
        for u, v in edges:
            in_degrees[v] += 1

        winner = -1

        for node in range(n):
            if in_degrees[node] == 0:
                if winner != -1:
                    return -1
                else:
                    winner = node
        return winner
