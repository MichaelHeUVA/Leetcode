# https://leetcode.com/problems/distance-to-a-cycle-in-undirected-graph/description/?envType=weekly-question&envId=2024-11-29
from collections import defaultdict, deque
from typing import List


class Solution:
    def distanceToCycle(self, n: int, edges: List[List[int]]) -> List[int]:
        adj_list = defaultdict(list)
        in_degree = [0] * n
        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)
            in_degree[u] += 1
            in_degree[v] += 1

        node_in_cycle = [True] * n
        q = deque()
        for node in range(n):
            if in_degree[node] == 1:
                q.append(node)

        while q:
            node = q.popleft()
            node_in_cycle[node] = False

            for neighbor in adj_list[node]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 1:
                    q.append(neighbor)

        visited = [False] * n
        output = [0] * n
        for node in range(n):
            if node_in_cycle[node]:
                q.append(node)
                visited[node] = True

        d = 0
        while q:
            size = len(q)
            for _ in range(size):
                node = q.popleft()
                output[node] = d
                visited[node] = True

                for neighbor in adj_list[node]:
                    if not visited[neighbor]:
                        q.append(neighbor)
            d += 1

        return output
