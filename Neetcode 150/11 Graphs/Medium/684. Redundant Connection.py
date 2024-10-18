# https://leetcode.com/problems/redundant-connection/description/
from collections import defaultdict
from typing import List


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)

        visited = [False] * (len(edges) + 1)

        def search(node, target):
            if node == target:
                return True
            if visited[node]:
                return False
            visited[node] = True
            for neighbor in graph[node]:
                if search(neighbor, target):
                    return True
            return False

        for edge in edges:
            a = edge[0]
            b = edge[1]
            if search(a, b):
                return [a, b]
            graph[a].append(b)
            graph[b].append(a)
            visited = [False] * (len(edges) + 1)
