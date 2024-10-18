# https://leetcode.com/problems/clone-graph/description/
from typing import Optional


# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:
        completed_node = {}

        def dfs(node):
            if node in completed_node:
                return completed_node[node]
            copy = Node(node.val)
            completed_node[node] = copy
            for neighbor in node.neighbors:
                copy.neighbors.append(dfs(neighbor))
            return copy

        return dfs(node) if node else None
