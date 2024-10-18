# https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/description/
from typing import List


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        def find(i):
            if parent[i] != i:
                parent[i] = find(parent[i])
            return parent[i]

        parent = list(range(n))
        for a, b in edges:
            parent[find(a)] = find(b)
        return sum(i == find(i) for i in range(n))
