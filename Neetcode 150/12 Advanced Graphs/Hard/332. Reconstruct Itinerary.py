# https://leetcode.com/problems/reconstruct-itinerary/description/
from collections import defaultdict
from typing import List


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj_list = defaultdict(list)
        for start, end in tickets:
            adj_list[start].append(end)
        for key in adj_list:
            adj_list[key].sort(reverse=True)

        def dfs(node):
            while adj_list[node]:
                neighbor = adj_list[node][-1]
                adj_list[node].pop()
                dfs(neighbor)
            output.append(node)

        output = []
        dfs("JFK")
        return list(reversed(output))
