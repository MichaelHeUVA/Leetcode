# https://leetcode.com/problems/valid-arrangement-of-pairs/description/?envType=daily-question&envId=2024-11-30
from collections import defaultdict, deque
from typing import List


class Solution:
    def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:
        adj_list = defaultdict(deque)
        in_degree = defaultdict(int)
        out_degree = defaultdict(int)
        for u, v in pairs:
            adj_list[u].append(v)
            out_degree[u] += 1
            in_degree[v] += 1

        output = []

        def dfs(node):
            while adj_list[node]:
                neighbor = adj_list[node].popleft()
                dfs(neighbor)
            output.append(node)

        start_node = -1
        for node in out_degree:
            if out_degree[node] == in_degree[node] + 1:
                start_node = node
                break
        if start_node == -1:
            start_node = pairs[0][0]

        dfs(start_node)

        output.reverse()

        output = [[output[i - 1], output[i]] for i in range(1, len(output))]

        return output
